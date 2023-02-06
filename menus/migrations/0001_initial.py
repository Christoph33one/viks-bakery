# Generated by Django 3.2.16 on 2023-01-25 16:44

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CakeItem',
            fields=[
                ('cake_id', models.AutoField(primary_key=True, serialize=False)),
                ('cake_name', models.CharField(max_length=80, unique=True)),
                ('description', models.CharField(max_length=200, unique=True)),
                ('dietary', models.CharField(max_length=200)),
                ('allergens', models.CharField(max_length=200, null=True)),
                ('featured_image', cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image')),
                ('on_menu', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]