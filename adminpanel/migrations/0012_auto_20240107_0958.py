# Generated by Django 3.2.13 on 2024-01-07 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0011_complain_details_complaints_info'),
    ]

    operations = [
        migrations.DeleteModel(
            name='complain_details',
        ),
        migrations.DeleteModel(
            name='complaints_info',
        ),
    ]
