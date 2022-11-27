# Generated by Django 4.1.3 on 2022-11-27 15:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_instructor_course_instructor'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='lesson_number',
            field=models.PositiveBigIntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]