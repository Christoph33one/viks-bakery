# Generated by Django 3.2.16 on 2023-01-28 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0003_creamcakes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cakeitem',
            name='cake_selections',
            field=models.IntegerField(choices=[(0, 'Chocolate Cakes'), (1, 'Cream cakes'), (1, 'New item')], default=2),
        ),
        migrations.AlterField(
            model_name='creamcakes',
            name='cake_selections',
            field=models.IntegerField(choices=[(0, 'Cream Cakes'), (1, 'New item')], default=1),
        ),
    ]