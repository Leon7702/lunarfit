from django.contrib import admin

from .models import Sport, Trs, Workout


class SportAdmin(admin.ModelAdmin):
    model = Sport
    list_display = ["name", "id"]
    readonly_fields = ["id"]


class TrsAdmin(admin.ModelAdmin):
    model = Trs
    list_display = [field.name for field in model._meta.fields]
    list_filter = [
        ("user", admin.RelatedOnlyFieldListFilter),
    ]
    readonly_fields = ["acwr", "trs_acwr"]


class WorkoutAdmin(admin.ModelAdmin):
    model = Workout
    list_display = [field.name for field in model._meta.fields]
    list_filter = [
        ("user", admin.RelatedOnlyFieldListFilter),
        ("sport", admin.RelatedOnlyFieldListFilter),
    ]


admin.site.register(Sport, SportAdmin)
admin.site.register(Trs, TrsAdmin)
admin.site.register(Workout, WorkoutAdmin)
