# Generated by Django 3.2.6 on 2021-11-22 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="eventdelivery",
            options={"ordering": ("-created_at",)},
        ),
        migrations.AlterModelOptions(
            name="eventdeliveryattempt",
            options={"ordering": ("-created_at",)},
        ),
    ]
