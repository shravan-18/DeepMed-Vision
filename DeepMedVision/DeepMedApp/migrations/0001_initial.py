# Generated by Django 5.0.7 on 2024-10-04 09:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Patient",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="John Doe", max_length=100)),
                ("age", models.IntegerField(default=30)),
                ("gender", models.CharField(default="Male", max_length=10)),
                (
                    "contact_number",
                    models.CharField(default="1234567890", max_length=15),
                ),
                (
                    "diagnosis",
                    models.CharField(default="Not Diagnosed", max_length=255),
                ),
            ],
        ),
    ]
