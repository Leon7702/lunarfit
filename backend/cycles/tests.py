from datetime import date

from rest_framework import status
from rest_framework.test import APITestCase

from .models import User, Type, TrackingData, MenstrualCycle, Phase, Onboarding


class TrackingDataTest(APITestCase):

    fixtures = ["contraceptives",
                "medication_data",
                "type_data"]

    def setUp(self):
        self.user0 = User.objects.create_user(email='user0@email.com', password='user0')
        self.user1 = User.objects.create_user(email='user1@email.com', password='user1')
        self.user2 = User.objects.create_user(email='user2@email.com', password='user2')
        self.user3 = User.objects.create_user(email='user3@email.com', password='user3')
        self.user4 = User.objects.create_user(email='user4@email.com', password='user4')

        self.type3 = Type.objects.create(name='cervix')
        self.type4 = Type.objects.create(name='cervix_mucus')

    def test_logging_tracking_data(self):
        self.client.force_authenticate(user=self.user0)

        response = self.client.post('/api/cycles/log/', {
            'user': self.user0.id,
            'type': self.type3.id,
            'date': date(2024, 7, 27),
            'value': 2.0
        })

        assert response.status_code == status.HTTP_201_CREATED
        assert TrackingData.objects.filter(user=self.user0, date=date(2024, 7, 27)).exists()


    def test_retrieving_logged_tracking_data(self):
        self.client.force_authenticate(user=self.user1)

        response = self.client.post('/api/cycles/log/', {
            'user': self.user1.id,
            'type': self.type3.id,
            'date': date(2024, 7, 27),
            'value': 2.0
        })

        assert response.status_code == status.HTTP_201_CREATED

        tracking_data_id = response.data['id']
        retrieve_response = self.client.get(f'/api/cycles/log/{tracking_data_id}/')
        assert retrieve_response.status_code == status.HTTP_200_OK

        response_data = retrieve_response.json()
        assert response_data['id'] == tracking_data_id


    def test_patching_logged_tracking_data(self):
        self.client.force_authenticate(user=self.user2)

        response = self.client.post('/api/cycles/log/', {
            'user': self.user2.id,
            'type': self.type4.id,
            'date': date(2024, 7, 27),
            'value': 2.0
        })

        assert response.status_code == status.HTTP_201_CREATED
        tracking_data_id = response.data['id']

        patch_response = self.client.patch(f'/api/cycles/log/{tracking_data_id}/', {
            'value': 3.0
        }, format='json')

        assert patch_response.status_code == status.HTTP_200_OK
        
        updated_tracking_data = TrackingData.objects.get(id=tracking_data_id)
        
        assert updated_tracking_data.value == 3.0


    def test_delete_tracking_data(self):
        self.client.force_authenticate(user=self.user3)

        response = self.client.post('/api/cycles/log/', {
            'user': self.user3.id,
            'type': self.type4.id,
            'date': date(2024, 6, 11),
            'value': 2.0
        })

        assert response.status_code == status.HTTP_201_CREATED
        tracking_data_id = response.data['id']

        delete_response = self.client.delete(f'/api/cycles/log/{tracking_data_id}/')
        assert delete_response.status_code == status.HTTP_204_NO_CONTENT

        assert not TrackingData.objects.filter(id=tracking_data_id).exists()


    def test_no_empty_values(self):
        self.client.force_authenticate(user=self.user4)

        response = self.client.post('/api/cycles/log/', {
            'user': self.user3.id,
            'type': self.type4.id,
            'date': date(2024, 5, 11),
            'value': ""
        })

        assert response.status_code == status.HTTP_400_BAD_REQUEST


class MenstrualCycleTest(APITestCase):

    fixtures = ["contraceptives",
                "medication_data",
                "type_data"]

    def setUp(self):
        self.user0 = User.objects.create_user(email='user0@email.com', password='user0')
        self.user1 = User.objects.create_user(email='user1@email.com', password='user1')
        self.user2 = User.objects.create_user(email='user2@email.com', password='user2')
        self.user3 = User.objects.create_user(email='user3@email.com', password='user3')
        self.user4 = User.objects.create_user(email='user4@email.com', password='user4')
        self.user5 = User.objects.create_user(email='user5@email.com', password='user5')
        self.user6 = User.objects.create_user(email='user6@email.com', password='user6')

        self.type1 = Type.objects.get(name='menstruation')
        self.type2 = Type.objects.get(name='temperature')
        self.type3 = Type.objects.get(name='cervix')
        self.type6 = Type.objects.get(name='ovulation_test')

    def test_new_cycle_if_entry_type1_and_no_mens_prev_day(self):
        """Create new cycle if user(s) 
            - has no tracking data of type 1 the day before
            - current cycle startet longer than 14 days ago
            - does not enough cycles (6) to not rely on onboarding values
        """
        self.client.force_authenticate(user=self.user0)

        Onboarding.objects.create(
            user=self.user0,
            workout_frequency=3,
            workout_duration=90,
            workout_intensity=5,
            cycle_duration=26,
            menstruation_duration=4
        )

        menstrual_cycle = MenstrualCycle.objects.create(
            user=self.user0,
            start=date(2024, 7, 4),
            end=date(2024, 7, 29)
        )       
        menstrual_cycles = MenstrualCycle.objects.filter(user=self.user0)
        assert menstrual_cycles.count() == 1

        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=0, start=date(2024, 7, 4), end=date(2024, 7, 8), avg_duration = 5)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=1, start=date(2024, 7, 9), end=date(2024, 7, 17),  avg_duration = 8)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=2, start=date(2024, 7, 18), end=date(2024, 7, 18),  avg_duration = 1)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=3, start=date(2024, 7, 19), end=date(2024, 7, 24), avg_duration = 9)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=4, start=date(2024, 7, 25), end=date(2024, 7, 29), avg_duration = 5)

        assert not TrackingData.objects.filter(user=self.user0, type=self.type1.id, date=date(2024, 7, 26)).exists()

        response = self.client.post('/api/cycles/log/', {
            'user': self.user0.id,
            'type': self.type1.id,
            'date': date(2024, 7, 27),
            'value': 2.0
        })

        assert response.status_code == status.HTTP_201_CREATED
        assert TrackingData.objects.filter(user=self.user0, date=date(2024, 7, 27)).exists()

        menstrual_cycles = MenstrualCycle.objects.filter(user=self.user0)
        assert menstrual_cycles.count() == 2

        new_cycle = menstrual_cycles.order_by('-start').first()
        assert new_cycle.start == date(2024, 7, 27)


    def test_adjust_old_cycle_and_phase_length_if_shorter_than_expected(self):
        self.client.force_authenticate(user=self.user3)

        Onboarding.objects.create(
            user=self.user3,
            workout_frequency=3,
            workout_duration=90,
            workout_intensity=5,
            cycle_duration=26,
            menstruation_duration=4
        )

        menstrual_cycle = MenstrualCycle.objects.create(
            user=self.user3,
            start=date(2024, 7, 4),
            end=date(2024, 7, 29)
        )

        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=0, start=date(2024, 7, 4), end=date(2024, 7, 8), avg_duration = 5)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=1, start=date(2024, 7, 9), end=date(2024, 7, 14), avg_duration = 6)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=2, start=date(2024, 7, 15), end=date(2024, 7, 15), avg_duration = 1)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=3, start=date(2024, 7, 16), end=date(2024, 7, 24), avg_duration = 9)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=4, start=date(2024, 7, 25), end=date(2024, 7, 29), avg_duration = 5)

        menstrual_cycles = MenstrualCycle.objects.filter(user=self.user3)
        assert menstrual_cycles.count() == 1

        response = self.client.post('/api/cycles/log/', {
            'user': self.user3.id,
            'type': self.type1.id,
            'date': date(2024, 7, 26),
            'value': 2.0
        })

        assert response.status_code == status.HTTP_201_CREATED

        menstrual_cycles = MenstrualCycle.objects.filter(user=self.user3).order_by('start')
        assert menstrual_cycles.count() == 2

        old_cycle = menstrual_cycles.first()
        assert old_cycle.end == date(2024, 7, 25)

        last_phase = Phase.objects.filter(cycle_id=old_cycle).order_by('-end').first()
        assert last_phase.end == date(2024, 7, 25)

        new_cycle = menstrual_cycles.last()
        assert new_cycle.start == date(2024, 7, 26)


    def test_adjust_old_cycle_and_phase_length_if_longer_than_expected(self):
        self.client.force_authenticate(user=self.user4)

        Onboarding.objects.create(
            user=self.user4,
            workout_frequency=3,
            workout_duration=90,
            workout_intensity=5,
            cycle_duration=26,
            menstruation_duration=4
        )

        menstrual_cycle = MenstrualCycle.objects.create(
            user=self.user4,
            start=date(2024, 7, 4),
            end=date(2024, 7, 29)
        )

        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=0, start=date(2024, 7, 4), end=date(2024, 7, 8), avg_duration = 5)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=1, start=date(2024, 7, 9), end=date(2024, 7, 14), avg_duration = 6)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=2, start=date(2024, 7, 15), end=date(2024, 7, 15), avg_duration = 1)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=3, start=date(2024, 7, 16), end=date(2024, 7, 24), avg_duration = 9)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=4, start=date(2024, 7, 25), end=date(2024, 7, 29), avg_duration = 5)

        menstrual_cycles = MenstrualCycle.objects.filter(user=self.user4)
        assert menstrual_cycles.count() == 1

        response = self.client.post('/api/cycles/log/', {
            'user': self.user4.id,
            'type': self.type1.id,
            'date': date(2024, 8, 14),
            'value': 2.0
        })

        assert response.status_code == status.HTTP_201_CREATED

        menstrual_cycles = MenstrualCycle.objects.filter(user=self.user4).order_by('start')
        assert menstrual_cycles.count() == 2

        old_cycle = menstrual_cycles.first()
        assert old_cycle.end == date(2024, 8, 13)

        last_phase = Phase.objects.filter(cycle_id=old_cycle).order_by('-end').first()
        assert last_phase.end == date(2024, 8, 13)

        new_cycle = menstrual_cycles.last()
        assert new_cycle.start == date(2024, 8, 14)


    def test_temperature_tracking_results_in_ovulation_next_day(self):
        self.client.force_authenticate(user=self.user1)

        menstrual_cycle = MenstrualCycle.objects.create(
            user=self.user1,
            start=date(2024, 7, 27),
            end=date(2024, 8, 23)
        )

        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=0, start=date(2024, 7, 27), end=date(2024, 7, 31), avg_duration = 5)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=1, start=date(2024, 8, 1),  end=date(2024, 8, 8),  avg_duration = 8)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=2, start=date(2024, 8, 9),  end=date(2024, 8, 9),  avg_duration = 1)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=3, start=date(2024, 8, 10), end=date(2024, 8, 18), avg_duration = 9)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=4, start=date(2024, 8, 19), end=date(2024, 8, 23), avg_duration = 5)

        tracking_data_entries = [
            {'date': date(2024, 8, 2), 'value': 36.2},
            {'date': date(2024, 8, 3), 'value': 36.2},
            {'date': date(2024, 8, 4), 'value': 36.2},
            {'date': date(2024, 8, 5), 'value': 36.2},
            {'date': date(2024, 8, 6), 'value': 36.2},
            {'date': date(2024, 8, 7), 'value': 36.2},
            {'date': date(2024, 8, 8), 'value': 36.4},
            {'date': date(2024, 8, 9), 'value': 36.4},
            {'date': date(2024, 8, 10), 'value': 36.4},
        ]
    
        for entry in tracking_data_entries:
            TrackingData.objects.create(
                user=self.user1,
                type=self.type2,
                date=entry['date'],
                value=entry['value']
            )
            
        phase_2 = Phase.objects.get(cycle_id=menstrual_cycle.id, phase_number=2)
        assert phase_2.start == date(2024, 8, 7)


    def test_positive_ovulation_test(self):
        self.client.force_authenticate(user=self.user2)

        menstrual_cycle = MenstrualCycle.objects.create(
            user=self.user2,
            start=date(2024, 7, 27),
            end=date(2024, 8, 23)
        )

        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=0, start=date(2024, 7, 27), end=date(2024, 7, 31), avg_duration = 5)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=1, start=date(2024, 8, 1),  end=date(2024, 8, 8),  avg_duration = 8)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=2, start=date(2024, 8, 9),  end=date(2024, 8, 9),  avg_duration = 1)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=3, start=date(2024, 8, 10), end=date(2024, 8, 18), avg_duration = 9)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=4, start=date(2024, 8, 19), end=date(2024, 8, 23), avg_duration = 5)

        response = self.client.post('/api/cycles/log/', {
            'user': self.user2.id,
            'type': self.type6.id,
            'date': date(2024, 8, 11),
            'value': 0.0
        })

        assert response.status_code == status.HTTP_201_CREATED

        menstrual_cycle = MenstrualCycle.objects.get(user=self.user2)

        phase_2 = Phase.objects.get(cycle_id=menstrual_cycle.id, phase_number=2)
        assert phase_2.start == date(2024, 8, 12)


    def test_adjust_phases_if_ovulation_detected(self):
        self.client.force_authenticate(user=self.user5)
        
        menstrual_cycle = MenstrualCycle.objects.create(
            user=self.user5,
            start=date(2024, 5, 1),
            end=date(2024, 5, 26)
        )

        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=0, start=date(2024, 5, 1), end=date(2024, 5, 5), avg_duration = 5)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=1, start=date(2024, 5, 6),  end=date(2024, 5, 11),  avg_duration = 6)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=2, start=date(2024, 5, 12),  end=date(2024, 5, 12),  avg_duration = 1)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=3, start=date(2024, 5, 13), end=date(2024, 5, 21), avg_duration = 9)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=4, start=date(2024, 5, 22), end=date(2024, 5, 26), avg_duration = 5)

        response = self.client.post('/api/cycles/log/', {
            'user': self.user5.id,
            'type': self.type6.id,
            'date': date(2024, 5, 8),
            'value': 0.0
        })

        assert response.status_code == status.HTTP_201_CREATED       

        phase_1 = Phase.objects.get(cycle_id=menstrual_cycle.id, phase_number=1)
        assert phase_1.end == date(2024, 5, 8)

        phase_2 = Phase.objects.get(cycle_id=menstrual_cycle.id, phase_number=2)
        assert phase_2.start == date(2024, 5, 9)
        assert phase_2.end == date(2024, 5, 9)

        phase_3 = Phase.objects.get(cycle_id=menstrual_cycle.id, phase_number=3)
        assert phase_3.start == date(2024, 5, 10)
        assert phase_3.end == date(2024, 5, 18)

        phase_4 = Phase.objects.get(cycle_id=menstrual_cycle.id, phase_number=4)
        assert phase_4.start == date(2024, 5, 19)
        assert phase_4.end == date(2024, 5, 23)


    def test_cycle_mens_over_for_new_user(self):
        self.client.force_authenticate(user=self.user6)

        # Onboarding.objects.create(
        #     user=self.user6,
        #     workout_frequency=3,
        #     workout_duration=90,
        #     workout_intensity=5,
        #     cycle_duration=26,
        #     menstruation_duration=5
        # )

        response = self.client.post('/api/users/onboarding/', {
            'user': self.user6.id,
            'timestamp': date(2024, 8, 1),
            'workout_frequency': 4,
            'workout_duration': 90,
            'workout_intensity' : 7,
            'cycle_duration' : 30,
            'menstruation_duration' : 5
        })

        assert response.status_code == status.HTTP_201_CREATED       

        menstrual_cycle = MenstrualCycle.objects.create(
            user=self.user6,
            start=date(2024, 7, 27),
            end=date(2024, 8, 23)
        )

        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=0, start=date(2024, 7, 27), end=date(2024, 7, 31), avg_duration = 5)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=1, start=date(2024, 8, 1),  end=date(2024, 8, 8),  avg_duration = 8)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=2, start=date(2024, 8, 9),  end=date(2024, 8, 9),  avg_duration = 1)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=3, start=date(2024, 8, 10), end=date(2024, 8, 18), avg_duration = 9)
        Phase.objects.create(cycle_id=menstrual_cycle, phase_number=4, start=date(2024, 8, 19), end=date(2024, 8, 23), avg_duration = 5)

        response = self.client.post('/api/cycles/log/', {
            'user': self.user6.id,
            'type': self.type1.id,
            'date': date(2024, 8, 1),
            'value': 2.0
        })

        assert response.status_code == status.HTTP_201_CREATED       

        phase_0 = Phase.objects.get(cycle_id=menstrual_cycle.id, phase_number=0)
        assert phase_0.end == date(2024, 8, 1)