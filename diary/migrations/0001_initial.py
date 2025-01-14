# Generated by Django 5.1.4 on 2024-12-30 12:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cuisine",
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
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("views", models.IntegerField(blank=True, default=0, null=True)),
            ],
        ),
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
                (
                    "photo",
                    models.ImageField(
                        blank=True, null=True, upload_to="cuisine_photos/"
                    ),
                ),
                (
                    "cuisine",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="diary.cuisine",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Restaurant",
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
                ("name", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("city", models.CharField(max_length=100)),
                (
                    "contact_info",
                    models.CharField(blank=True, max_length=50, null=True),
                ),
                ("website", models.URLField(blank=True, null=True)),
                ("opening_time", models.TimeField()),
                ("closing_time", models.TimeField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "cuisines",
                    models.ManyToManyField(
                        related_name="restaurants", to="diary.cuisine"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RestaurantPhoto",
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
                ("photo", models.ImageField(upload_to="restaurant_photos/")),
                ("uploaded_at", models.DateTimeField(auto_now_add=True)),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="photos",
                        to="diary.restaurant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Review",
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
                ("comment", models.TextField()),
                (
                    "rating",
                    models.DecimalField(
                        decimal_places=1,
                        help_text="Rating between 0.0 and 5.0",
                        max_digits=2,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "restaurant",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews",
                        to="diary.restaurant",
                    ),
                ),
                (
                    "visitor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="restaurant_reviews",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="VisitorProfile",
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
                ("name", models.CharField(blank=True, max_length=255, null=True)),
                ("place", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "contact_info",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                (
                    "preferred_cuisine",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="preferred_by_visitors",
                        to="diary.cuisine",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="visitorprofile",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Visit",
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
                ("expense", models.DecimalField(decimal_places=2, max_digits=10)),
                ("comment", models.TextField()),
                (
                    "rating",
                    models.DecimalField(
                        decimal_places=1,
                        help_text="Rating between 0.0 and 5.0",
                        max_digits=3,
                    ),
                ),
                ("visit_date", models.DateTimeField(auto_now_add=True)),
                (
                    "cuisine",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="ordered_visits",
                        to="diary.cuisine",
                    ),
                ),
                (
                    "visitor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="visits",
                        to="diary.visitorprofile",
                    ),
                ),
            ],
        ),
    ]
