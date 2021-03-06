# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-20 08:12
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=30, unique=True, verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('profile', models.CharField(blank=True, max_length=255, verbose_name='profile')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('birthday', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('man', '男性'), ('woman', '女性'), ('unknown', 'その他')], max_length=10)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'api_user',
                'swappable': 'AUTH_USER_MODEL',
            },
        ),
        migrations.CreateModel(
            name='RoutePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('desc', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RoutePlanSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_num', models.IntegerField()),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('finish_time', models.TimeField(blank=True, null=True)),
                ('route_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='route_plan', to='travelplan.RoutePlan')),
            ],
        ),
        migrations.CreateModel(
            name='TourismSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('desc', models.CharField(blank=True, max_length=1000, null=True)),
                ('prefecture', models.CharField(max_length=9)),
                ('address', models.CharField(blank=True, max_length=80, null=True)),
                ('phone_num', models.CharField(blank=True, max_length=12, null=True)),
                ('parkinglot', models.IntegerField(blank=True, null=True)),
                ('holiday', models.CharField(blank=True, max_length=7, null=True)),
                ('business_hours', models.CharField(blank=True, max_length=11, null=True)),
                ('charge', models.PositiveIntegerField(blank=True, null=True)),
                ('coordinate_latitude', models.FloatField(blank=True, null=True)),
                ('coordinate_longitude', models.FloatField(blank=True, null=True)),
                ('grade', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
            ],
        ),
        migrations.AddField(
            model_name='routeplanspot',
            name='spot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='spot', to='travelplan.TourismSpot'),
        ),
    ]
