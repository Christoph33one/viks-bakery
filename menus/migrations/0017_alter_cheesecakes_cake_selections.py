# Generated by Django 3.2.16 on 2023-02-15 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0016_alter_cheesecakes_cake_selections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cheesecakes',
            name='cake_selections',
            field=models.IntegerField(choices=[(0, 'Cheese Cakes'), (2, 'New item'), (1, 'Vegan Cakes')], default=3),
        ),
    ]
