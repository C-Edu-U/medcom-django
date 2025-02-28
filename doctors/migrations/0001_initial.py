# Generated by Django 4.2.9 on 2025-01-31 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("patients", "0003_person_delete_patient"),
    ]

    operations = [
        migrations.CreateModel(
            name="Doctor",
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
                (
                    "person",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="patients.person",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Specialization",
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
                ("name", models.CharField(max_length=100, unique=True)),
                ("description", models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="DoctorSpecialization",
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
                ("graduation_date", models.DateField()),
                (
                    "doctor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="doctors.doctor"
                    ),
                ),
                (
                    "specialization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="doctors.specialization",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="doctor",
            name="specializations",
            field=models.ManyToManyField(
                through="doctors.DoctorSpecialization", to="doctors.specialization"
            ),
        ),
    ]
