# Generated by Django 3.0.5 on 2020-04-10 06:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("core", "0001_initial"),
        ("analytics", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="session",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="core.Service"
            ),
        ),
        migrations.AddField(
            model_name="hit",
            name="session",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="analytics.Session"
            ),
        ),
    ]
