# Generated by Django 4.2.9 on 2024-01-18 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
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
                ("firstname", models.TextField(blank=True, null=True)),
                ("lastname", models.TextField(blank=True, null=True)),
            ],
            options={
                "db_table": "user_table",
            },
        ),
    ]
