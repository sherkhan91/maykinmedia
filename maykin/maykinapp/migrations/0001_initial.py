# Generated by Django 3.1.1 on 2021-08-07 12:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_code', models.CharField(default='CIT', max_length=3, unique=True)),
                ('city_name', models.CharField(default='Default City', max_length=86, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_hotel_code', models.CharField(default='CHC', max_length=3, unique=True)),
                ('hotel_name', models.TextField(default='Default hotel name', unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maykinapp.city')),
            ],
        ),
    ]
