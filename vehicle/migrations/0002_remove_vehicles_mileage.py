# Generated by Django 4.2.4 on 2023-09-25 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("vehicle", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="vehicles", name="mileage",),
    ]