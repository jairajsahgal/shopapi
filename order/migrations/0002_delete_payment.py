# Generated by Django 4.1.7 on 2023-04-17 08:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("order", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Payment",
        ),
    ]
