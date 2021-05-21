# Generated by Django 3.2.3 on 2021-05-15 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("two_salmon", "0007_auto_20210515_0958"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shift",
            name="wave_1_event_type",
            field=models.CharField(
                choices=[
                    ("cohock-charge", "Cohock Charge"),
                    ("fog", "Fog"),
                    ("griller", "The Griller"),
                    ("goldie-seeking", "Goldie Seeking"),
                    ("rush", "Rush"),
                    ("the-mothership", "The Mothership"),
                    ("water-levels", "-"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="shift",
            name="wave_2_event_type",
            field=models.CharField(
                choices=[
                    ("cohock-charge", "Cohock Charge"),
                    ("fog", "Fog"),
                    ("griller", "The Griller"),
                    ("goldie-seeking", "Goldie Seeking"),
                    ("rush", "Rush"),
                    ("the-mothership", "The Mothership"),
                    ("water-levels", "-"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="shift",
            name="wave_3_event_type",
            field=models.CharField(
                choices=[
                    ("cohock-charge", "Cohock Charge"),
                    ("fog", "Fog"),
                    ("griller", "The Griller"),
                    ("goldie-seeking", "Goldie Seeking"),
                    ("rush", "Rush"),
                    ("the-mothership", "The Mothership"),
                    ("water-levels", "-"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]