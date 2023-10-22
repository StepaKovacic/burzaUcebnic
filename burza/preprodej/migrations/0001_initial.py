# Generated by Django 4.2.6 on 2023-10-22 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Book",
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
                ("name", models.CharField(max_length=200)),
                ("img_url", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Offer",
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
                ("description", models.CharField(max_length=500)),
                ("state", models.IntegerField()),
                ("contact_info", models.CharField(max_length=200)),
                (
                    "book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="preprodej.book"
                    ),
                ),
            ],
        ),
    ]