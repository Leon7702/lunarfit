from django.contrib import admin
from .models import MenstrualCycle, Medication, MedicationCategory, TrackingData, Type, Phase

admin.site.register(MenstrualCycle)
admin.site.register(MedicationCategory)
admin.site.register(Medication)
admin.site.register(TrackingData)
admin.site.register(Type)
admin.site.register(Phase)
