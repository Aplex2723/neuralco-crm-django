# Generated by Django 3.1.7 on 2021-03-23 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0023_apisettings_company"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="company",
        ),
    ]