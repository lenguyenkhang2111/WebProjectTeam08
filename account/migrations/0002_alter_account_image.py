# Generated by Django 4.1.3 on 2022-12-23 05:33

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, default='account/profile_pics/doras.png', force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='account/profile_pics/'),
        ),
    ]
