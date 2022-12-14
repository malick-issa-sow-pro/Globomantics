# Generated by Django 4.0.6 on 2022-07-21 15:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_room', models.CharField(max_length=25)),
                ('floor', models.IntegerField()),
                ('number_of_room', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_meeting', models.CharField(max_length=200)),
                ('duration', models.TimeField(default=datetime.time(1, 0))),
                ('start_time', models.TimeField(default=datetime.time(9, 0))),
                ('date_meeting', models.DateField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='meeting.room')),
            ],
        ),
    ]
