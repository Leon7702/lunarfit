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

    def __str__(self):
        return f"{self.phase_number}, {self.cycle_id}"


class MedicationCategory(models.Model):
    name = models.CharField(max_length=50)


class Medication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    medication_id = models.ForeignKey(MedicationCategory, on_delete=models.CASCADE)


class Type(models.Model):
    name = models.CharField(max_length=24)

    

class TrackingData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    date = models.DateField()
    value = models.DecimalField(max_digits=4, decimal_places=2)


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

            if latest_cycle is None or (timezone.now().date() - latest_cycle.start).days >= 14 and not previous_day_entry:

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
                        phase_number=phase_number
                    )
                    
                    # Update current_start for the next phase
                    current_start = current_end + timezone.timedelta(days=1)

        #Temperature only tracking to determine phases
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

                current_cycle = MenstrualCycle.objects.filter(user=user).order_by('-start').first()

                if current_cycle:
                    phase_3 = Phase.objects.filter(cycle_id=current_cycle, phase_number=3).first()
                    phase_4 = Phase.objects.filter(cycle_id=current_cycle, phase_number=4).first()
                    phase_3_duration = (phase_3.end - phase_3.start).days + 1 if phase_3 else default_phase_lengths[3]
                    phase_4_duration = (phase_4.end - phase_4.start).days + 1 if phase_4 else default_phase_lengths[4]
                else:
                    phase_3_duration = default_phase_lengths[3]
                    phase_4_duration = default_phase_lengths[4]


                #Update Phases
                phase_2_start = low_temp_day
                phase_2_end = phase_2_start + timezone.timedelta(days=default_phase_lengths[2] - 1)

                phase_1_end = phase_2_start - timezone.timedelta(days=1)

                # Phase 3: Starts the day after Phase 2 ends, keeps avg duration
                phase_3_start = phase_2_end + timezone.timedelta(days=1)
                phase_3_end = phase_3_start + timezone.timedelta(days=phase_3_duration - 1)

                # Phase 4: Starts the day after Phase 3 ends, keeps avg duration
                phase_4_start = phase_3_end + timezone.timedelta(days=1)
                phase_4_end = phase_4_start + timezone.timedelta(days=phase_4_duration - 1)

                menstrual_cycle = current_cycle

                if menstrual_cycle:
                    Phase.objects.filter(cycle_id=menstrual_cycle, phase_number=1).update(
                        end=phase_1_end
                    )
                    Phase.objects.filter(cycle_id=menstrual_cycle, phase_number=2).update(
                        start=phase_2_start,
                        end=phase_2_end
                    )
                    Phase.objects.filter(cycle_id=menstrual_cycle, phase_number=3).update(
                        start=phase_3_start,
                        end=phase_3_end
                    )
                    Phase.objects.filter(cycle_id=menstrual_cycle, phase_number=4).update(
                        start=phase_4_start,
                        end=phase_4_end
                    )

                    #Update end of cycle
                    menstrual_cycle.end = phase_4_end
                    menstrual_cycle.save()


        #Combined phase determination via cervix and cervix mucus
        elif entry_type.id in [3, 4]:
            
            yesterday = start_date - timezone.timedelta(days=1)
            entries_yesterday = TrackingData.objects.filter(user=user, date=yesterday)
            entries_today = TrackingData.objects.filter(user=user, date=start_date)

            #Determine prior mucus values
            has_type_3_value_2_yesterday = entries_yesterday.filter(type=3, value=2).exists()
            has_type_4_value_4_yesterday = entries_yesterday.filter(type=4, value=4).exists()
            has_type_4_value_4_today = entries_today.filter(type=4, value=4).exists()
            has_type_3_value_2_today = entries_today.filter(type=3, value=2).exists()


            if (entry_type.id == 3 and instance.value == 2 and
                has_type_4_value_4_yesterday and has_type_4_value_4_today and has_type_3_value_2_yesterday) or \
            (entry_type.id == 4 and instance.value == 4 and
                has_type_3_value_2_yesterday and has_type_3_value_2_today and has_type_4_value_4_yesterday):

                #Conditions for Ovulation day the next day met
                phase_2_start = start_date + timezone.timedelta(days=1)
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

                    # Update phases
                    Phase.objects.filter(cycle_id=current_cycle, phase_number=1).update(end=phase_1_end)
                    Phase.objects.filter(cycle_id=current_cycle, phase_number=2).update(start=phase_2_start, end=phase_2_end)
                    Phase.objects.filter(cycle_id=current_cycle, phase_number=3).update(start=phase_3_start, end=phase_3_end)
                    Phase.objects.filter(cycle_id=current_cycle, phase_number=4).update(start=phase_4_start, end=phase_4_end)

                    # Update cycle end date
                    current_cycle.end = phase_4_end
                    current_cycle.save()