from django.contrib import admin
from .models import MenstrualCycle, Medication, MedicationCategory

admin.site.register(MenstrualCycle)
admin.site.register(MedicationCategory)
admin.site.register(Medication)
