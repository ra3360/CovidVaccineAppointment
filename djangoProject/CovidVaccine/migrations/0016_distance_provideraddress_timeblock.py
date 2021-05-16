# Generated by Django 3.2.1 on 2021-05-16 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CovidVaccine', '0015_alter_provider_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField()),
                ('pid', models.IntegerField()),
                ('distance', models.TextField()),
            ],
            options={
                'db_table': 'distance',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Provideraddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.IntegerField()),
                ('locationx', models.IntegerField()),
                ('locationy', models.IntegerField()),
            ],
            options={
                'db_table': 'provideraddress',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Timeblock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'db_table': 'timeblock',
                'managed': False,
            },
        ),
    ]
