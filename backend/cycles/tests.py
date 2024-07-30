from django.test import TestCase
from .models import User, Type, TrackingData, MenstrualCycle, Phase
from rest_framework.test import APITestCase
from datetime import date
from rest_framework import status

class MenstrualCycleTest(APITestCase):
    def setUp(self):
        self.user0 = User.objects.create_user(email='user0@email.com', password='user0')
        self.client.force_authenticate(user=self.user0) #needed?


    def test_new_cycle_if_entry_type1_and_no_mens_prev_day(self):
              
        self.type1 = Type.objects.create(name='Menstruation')

        response = self.client.post('/api/cycles/log/', {
            'user': self.user0.id,
            'type': self.type1.id,
            'date': date(2024, 8, 20),
            'value': 2.0
        })

        # Ensure the TrackingData entry is created successfully
        assert response.status_code == status.HTTP_201_CREATED
        assert TrackingData.objects.filter(user=self.user0, date=date(2024, 8, 20)).exists()

        # Check that no new MenstrualCycle is created
        menstrual_cycles = MenstrualCycle.objects.filter(user=self.user0)
        assert menstrual_cycles.count() == 1