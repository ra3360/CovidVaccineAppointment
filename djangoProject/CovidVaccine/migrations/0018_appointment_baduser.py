# Generated by Django 3.2.1 on 2021-05-17 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CovidVaccine', '0017_provideravailability_providertravellimit_providerweeklock_useravailability_usertravellimit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.IntegerField()),
                ('slotid', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('user_accepted', models.CharField(max_length=20)),
                ('user_canceled', models.CharField(blank=True, max_length=20, null=True)),
                ('user_showedup', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'appointment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Baduser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.IntegerField()),
            ],
            options={
                'db_table': 'baduser',
                'managed': False,
            },
        ),
    ]