# Generated by Django 3.2.13 on 2023-12-31 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminpanel', '0003_customerrepository_dob'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerrepository',
            name='Age',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='Balance',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='CardNo',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='CardType',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='Complain',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='CreditScore',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='CustomerId',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='DOB',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='EstimatedSalary',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='Exited',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='Gender',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='Geography',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='HasCrCard',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='IsActiveMember',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='Mobile',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='NumOfProducts',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='PointEarned',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='RowNumber',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='SatisfactionScore',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='Surname',
        ),
        migrations.RemoveField(
            model_name='customerrepository',
            name='Tenure',
        ),
    ]
