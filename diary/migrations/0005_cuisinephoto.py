# Generated by Django 5.1.4 on 2024-12-07 08:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("diary", "0004_rename_resturant_visit_restaurant"),
    ]

    operations = [
        migrations.CreateModel(
            name="CuisinePhoto",
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
                ("photo", models.ImageField(upload_to="cuisine_photos/")),
                ("description", models.TextField(blank=True)),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="cuisine_photos",
                        to="diary.restaurant",
                    ),
                ),
            ],
        ),
    ]
