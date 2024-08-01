from django.db import models

from users.models import User, Onboarding
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from decimal import Decimal


class MenstrualCycle(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()

    def __str__(self):
        return f"{self.user.email}"


class Phase(models.Model):
    PHASES = [
        (0, "Menstruation"),
        (1, "Follicular"),
        (2, "Ovulation"),
        (3, "Early Luteal"),
        (4, "Late Luteal"),
    ]
    cycle_id = models.ForeignKey(MenstrualCycle, related_name="phases", on_delete=models.CASCADE)
    start = models.DateField()
    end = models.DateField()
    phase_number = models.PositiveIntegerField(choices=PHASES)
    avg_duration = models.PositiveIntegerField()

    def get_phase_name(self):
        return dict(self.PHASES).get(self.phase_number, "")

    def __str__(self):
        return f"{self.phase_number}, {self.get_phase_name()}"


class MedicationCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    medication_id = models.ForeignKey(MedicationCategory, on_delete=models.CASCADE)


class Type(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return f"{self.pk}, {self.name}"

    

class TrackingData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.type.name}, {self.user}, {self.pk}"


@receiver(post_save, sender=TrackingData)
def create_or_update_menstrual_cycle(sender, instance, created, **kwargs):
    if created:
 
        user=instance.user
        start_date = instance.date
        tracking_value = instance.value
        entry_type = instance.type

        default_phase_lengths = {
            0: 5,  # Menstruation
            1: 8,  # Follicular
            2: 1,  # Ovulation
            3: 9,  # Early Luteal
            4: 5   # Late Luteal
        }

        #Mens tracking defines new cycle
        if entry_type.id == 1:
            latest_cycle = MenstrualCycle.objects.filter(user=user).order_by('-start').first()        
            previous_day = start_date - timezone.timedelta(days=1)
            previous_day_entry = TrackingData.objects.filter(user=user, type=1, date=previous_day).exists()

            if latest_cycle is None or (start_date - latest_cycle.start).days >= 14 and not previous_day_entry:
                latest_cycles = MenstrualCycle.objects.filter(user=user).order_by('-start')[:6]
                cycle_count = latest_cycles.count()
                if cycle_count >= 6: #6 or more cycles to determine avg values
                    cycle_duration = sum((cycle.end - cycle.start).days + 1 for cycle in latest_cycles) // cycle_count
                    phase_0_duration = sum((Phase.objects.filter(cycle_id=cycle.id, phase_number=0).first().end - Phase.objects.filter(cycle_id=cycle.id, phase_number=0).first().start).days + 1 for cycle in latest_cycles) // cycle_count
                    phase_3_duration = sum((Phase.objects.filter(cycle_id=cycle.id, phase_number=3).first().end - Phase.objects.filter(cycle_id=cycle.id, phase_number=3).first().start).days + 1 for cycle in latest_cycles) // cycle_count
                    phase_4_duration = sum((Phase.objects.filter(cycle_id=cycle.id, phase_number=4).first().end - Phase.objects.filter(cycle_id=cycle.id, phase_number=4).first().start).days + 1 for cycle in latest_cycles) // cycle_count
                elif cycle_count >= 1: #less than 6 cycles + onboarding to determine avg values
                    onboarding = Onboarding.objects.filter(user=user).first()
                    cycle_duration = (sum((cycle.end - cycle.start).days + 1 for cycle in latest_cycles) + onboarding.cycle_duration * (6 - cycle_count)) // 6
                    phase_0_duration = (sum((Phase.objects.filter(cycle_id=cycle.id, phase_number=0).first().end - Phase.objects.filter(cycle_id=cycle.id, phase_number=0).first().start).days + 1 for cycle in latest_cycles) + onboarding.menstruation_duration * (6 - cycle_count)) // 6
                    phase_3_duration = sum((Phase.objects.filter(cycle_id=cycle.id, phase_number=3).first().end - Phase.objects.filter(cycle_id=cycle.id, phase_number=3).first().start).days + 1 for cycle in latest_cycles) // cycle_count if cycle_count > 0 else default_phase_lengths[3]
                    phase_4_duration = sum((Phase.objects.filter(cycle_id=cycle.id, phase_number=4).first().end - Phase.objects.filter(cycle_id=cycle.id, phase_number=4).first().start).days + 1 for cycle in latest_cycles) // cycle_count if cycle_count > 0 else default_phase_lengths[4]
                else:
                    onboarding = Onboarding.objects.filter(user=user).first()
                    if onboarding: # no cycles, uses onboarding values
                        cycle_duration = onboarding.cycle_duration
                        phase_0_duration = onboarding.menstruation_duration
                        phase_3_duration = default_phase_lengths[3]
                        phase_4_duration = default_phase_lengths[4]
                    else: # no onboarding, default values
                        cycle_duration = default_phase_lengths[0] + default_phase_lengths[1] + default_phase_lengths[2] + default_phase_lengths[3] + default_phase_lengths[4]
                        phase_0_duration = default_phase_lengths[0]
                        phase_3_duration = default_phase_lengths[3]
                        phase_4_duration = default_phase_lengths[4]


                # Update the end dates of the last phase and cycle to be superseeded
                if latest_cycle:
                    last_phase = Phase.objects.filter(cycle_id=latest_cycle).order_by('-end').first()
                    if last_phase:
                        last_phase.end = start_date - timezone.timedelta(days=1)
                        last_phase.save()

                    latest_cycle.end = start_date - timezone.timedelta(days=1)
                    latest_cycle.save()

                # Phase 2 duration is always 1 day
                phase_2_duration = 1
                # Calculate phase 1 duration to fill the remaining days
                phase_1_duration = cycle_duration - (phase_0_duration + phase_2_duration + phase_3_duration + phase_4_duration)

                # Create the menstrual cycle
                end_date = start_date + timezone.timedelta(days=cycle_duration - 1)
                menstrual_cycle = MenstrualCycle.objects.create(
                    user=user,
                    start=start_date,
                    end=end_date
                )

                phases = [
                    (0, phase_0_duration),
                    (1, phase_1_duration),
                    (2, phase_2_duration),
                    (3, phase_3_duration),
                    (4, phase_4_duration)
                ]

                current_start = start_date

                #Calculate Phases
                for phase_number, duration in phases:
                    # Calculate end date to be inclusive
                    current_end = current_start + timezone.timedelta(days=duration - 1)
                    
                    Phase.objects.create(
                        cycle_id=menstrual_cycle,
                        start=current_start,
                        end=current_end,
                        phase_number=phase_number,
                        avg_duration=duration
                    )
                    
                    # Update current_start for the next phase
                    current_start = current_end + timezone.timedelta(days=1)

        #LH Messung
        elif entry_type.id == 6:
            if tracking_value in [1, 2]:
                return
            elif tracking_value == 0:
                update_phases(user, start_date + timezone.timedelta(days=1), default_phase_lengths)

        elif entry_type.id == 2:
            days_to_check = [start_date - timezone.timedelta(days=i) for i in range(8, -1, -1)]
            entries = TrackingData.objects.filter(user=user, type=2, date__in=days_to_check).order_by('date')

            if len(entries) < 9:
                return

            temperatures = [entry.value for entry in entries]
            
            if len(temperatures) != 9:
                return
            
            # Calculate the average temperature for the 6 days before temperature rise
            average_temp = sum(temperatures[:6]) / Decimal(6)

            # Last three days include the current day and two previous days
            last_three_temps = temperatures[6:]
           
            increase_threshold = Decimal('0.2')

            # Determine if the last three days' temperatures are all higher than average_temp + 0.2°C
            is_increase = all(temp >= average_temp + increase_threshold for temp in last_three_temps)

            if is_increase:
                # Ovulation is on last low temperature day
                low_temp_day = days_to_check[5]
                check_days = [low_temp_day - timezone.timedelta(days=i) for i in range(1, 3)]

                tracking_data_type_3 = TrackingData.objects.filter(user=user, type=3, date__in=check_days)
                tracking_data_type_4 = TrackingData.objects.filter(user=user, type=4, date__in=check_days)

                if not tracking_data_type_3.exists() or not tracking_data_type_4.exists():
                    update_phases(user, low_temp_day, default_phase_lengths)
                else:
                    type_3_values = list(tracking_data_type_3.values_list('value', flat=True))
                    type_4_values = list(tracking_data_type_4.values_list('value', flat=True))

                    if (type_3_values == [2, 2]) and (type_4_values == [4, 4]):
                        update_phases(user, low_temp_day, default_phase_lengths)
                    else:
                        return


def update_phases(user, low_temp_day, default_phase_lengths):
    phase_2_start = low_temp_day
    phase_2_end = phase_2_start + timezone.timedelta(days=default_phase_lengths[2] - 1)

    current_cycle = MenstrualCycle.objects.filter(user=user).order_by('-start').first()

    if current_cycle:
        phase_3 = Phase.objects.filter(cycle_id=current_cycle, phase_number=3).first()
        phase_4 = Phase.objects.filter(cycle_id=current_cycle, phase_number=4).first()
        phase_3_duration = (phase_3.end - phase_3.start).days + 1 if phase_3 else default_phase_lengths[3]
        phase_4_duration = (phase_4.end - phase_4.start).days + 1 if phase_4 else default_phase_lengths[4]

        phase_1_end = phase_2_start - timezone.timedelta(days=1)

        phase_3_start = phase_2_end + timezone.timedelta(days=1)
        phase_3_end = phase_3_start + timezone.timedelta(days=phase_3_duration - 1)
        phase_4_start = phase_3_end + timezone.timedelta(days=1)
        phase_4_end = phase_4_start + timezone.timedelta(days=phase_4_duration - 1)

        Phase.objects.filter(cycle_id=current_cycle, phase_number=1).update(end=phase_1_end)
        Phase.objects.filter(cycle_id=current_cycle, phase_number=2).update(start=phase_2_start, end=phase_2_end)
        Phase.objects.filter(cycle_id=current_cycle, phase_number=3).update(start=phase_3_start, end=phase_3_end)
        Phase.objects.filter(cycle_id=current_cycle, phase_number=4).update(start=phase_4_start, end=phase_4_end)

        current_cycle.end = phase_4_end
        current_cycle.save()