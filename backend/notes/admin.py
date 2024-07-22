from django.contrib import admin

from .models import Note, SymptomCategory, Symptom


admin.site.register(Symptom)
admin.site.register(SymptomCategory)
admin.site.register(Note)
