from django.contrib import admin

from .models import Sport, Trs, Workout

class SportAdmin(admin.ModelAdmin):
    model = Sport
    list_display = ["name", "id"]
    readonly_fields = ["id"]

admin.site.register(Sport, SportAdmin)
admin.site.register(Trs)
admin.site.register(Workout)
