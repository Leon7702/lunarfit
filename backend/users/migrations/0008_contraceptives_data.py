"""
Initial data migration of known contraceptive keywords,
see: https://docs.djangoproject.com/en/5.0/topics/migrations/#data-migrations
Note especially that the model is not imported directly, since it may change later.
It is instead called from the app registry to get the matching version.
"""

from django.db import migrations


def init_contraceptives(apps, schema_editor):

    # the indexes should never change in a future migration!
    # therefore they are explicit here
    CONTRACEPTIVES = {
        0: "pill",
        1: "spiral",
        2: "implant",
        3: "shot",
        4: "ring",
    }

    Contraceptive = apps.get_model("users", "Contraceptive")

    for id, name in CONTRACEPTIVES.items():
        contraceptive = Contraceptive(id=id, name=name)
        contraceptive.save()


class Migration(migrations.Migration):

    dependencies = [
        (
            "users",
            "0001_squashed_0007_rename_finished_onboarding_profile_onboarding_finished",
        ),
    ]

    operations = [
        migrations.RunPython(init_contraceptives),
    ]
