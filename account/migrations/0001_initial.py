# Generated by Django 4.1.3 on 2022-12-23 05:25

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(max_length=255)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('subscription_expired', models.DateField(blank=True, null=True)),
                ('image', django_resized.forms.ResizedImageField(blank=True, crop=None, default='doras.png', force_format=None, keep_meta=True, null=True, quality=100, scale=None, size=[1920, 1080], upload_to='account/profile_pics/')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superadmin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
