# Generated by Django 2.1.4 on 2018-12-12 11:18

import django.contrib.postgres.fields
from django.db import migrations, models
import rest_framework.compat
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalOpportunity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('scales', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(validators=[rest_framework.compat.MinValueValidator(0), rest_framework.compat.MaxValueValidator(100)]), size=6, validators=[rest_framework.compat.MinLengthValidator(6), rest_framework.compat.MinLengthValidator(6)])),
                ('activity', models.CharField(max_length=50)),
            ],
        ),
    ]