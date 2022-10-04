# Generated by Django 4.1.2 on 2022-10-04 23:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, unique=True)),
                ('description', models.CharField(max_length=120)),
                ('quantity', models.IntegerField(validators=[django.core.validators.MinValueValidator(limit_value=0, message='You have entered a value below the minimum'), django.core.validators.MaxValueValidator(limit_value=100, message='You have entered a value above the maximum')])),
            ],
        ),
    ]
