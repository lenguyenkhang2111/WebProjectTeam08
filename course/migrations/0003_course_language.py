# Generated by Django 4.1.3 on 2022-12-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_course_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='language',
            field=models.CharField(default='English', max_length=50),
        ),
    ]
