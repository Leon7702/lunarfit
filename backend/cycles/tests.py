from django.test import TestCase
from .models import User, Type, TrackingData, MenstrualCycle
from rest_framework.test import APITestCase
from datetime import date
from rest_framework import status

class MenstrualCycleTest(APITestCase):
    def setUp(self):
        self.user0 = User.objects.create_user(email='user0@email.com', password='user0')


    def test_no_new_cycle_if_prev_day_entry_type1_and_cycle_shorter_than_14_days(self):
         # Create a TrackingData entry for the previous day
        previous_day = date(2024-8-26)
        TrackingData.objects.create(
            user=self.user,
            type=1,
            date=previous_day,
            value=2.0
        )

         # Create a TrackingData entry for the current day
        response = self.client.post('/api/cycles/log/', {
            'user': self.user.id,
            'type': self.type.id,
            'date': date(2024-8-27),
            'value': 1.0
        })

        # Ensure the TrackingData entry is created successfully
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(TrackingData.objects.filter(user=self.user, date=date(2024-08-27)).exists())

        # Check that no new MenstrualCycle is created
        menstrual_cycles = MenstrualCycle.objects.filter(user=self.user)
        self.assertEqual(menstrual_cycles.count(), 0)