from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# List for chocolate cakes items in database
CAKE_SELECTIONS = (
    (0, "Chocolate Cakes"),
    (1, "Vegan Cakes"),
    (2, "New item"))

# List for cream cake items in database
CREAM_CAKE_SELECTIONS = (
    (0, "Cream Cakes"),
    (1, "Vegan Cakes"),
    (2, "New item")
    )

# List of cheese cake items in the database
CHEESE_CAKE_SELECTIONS = {
    (0, "Cheese Cakes"),
    (1, "Vegan Cakes"),
    (2, "New item")
}


# Choclate cake module
class CakeItem(models.Model):
    """model for admin cake list"""
    cake_id = models.AutoField(primary_key=True)
    cake_name = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=200, unique=True)
    dietary = models.CharField(max_length=200)
    allergens = models.CharField(max_length=200, null=True)
    cake_selections = models.IntegerField(
        choices=CAKE_SELECTIONS, default=3)
    featured_image = CloudinaryField('image', default='placeholder')
    on_menu = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ['-on_menu']

    def __str__(self):
        return self.cake_name


# Cream cake module
class CreamCakes(models.Model):
    """model for admin cake list"""
    cake_id = models.AutoField(primary_key=True)
    cake_name = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=200, unique=True)
    dietary = models.CharField(max_length=200)
    allergens = models.CharField(max_length=200, null=True)
    cake_selections = models.IntegerField(
        choices=CREAM_CAKE_SELECTIONS, default=3)
    featured_image = CloudinaryField('image', default='placeholder')
    on_menu = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ['-on_menu']

    def __str__(self):
        return self.cake_name


# Cheese cakes module
class CheeseCakes(models.Model):
    """model for admin cake list"""
    cake_id = models.AutoField(primary_key=True)
    cake_name = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=200, unique=True)
    dietary = models.CharField(max_length=200)
    allergens = models.CharField(max_length=200, null=True)
    cake_selections = models.IntegerField(
        choices=CHEESE_CAKE_SELECTIONS, default=3)
    featured_image = CloudinaryField('image', default='placeholder')
    on_menu = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ['-on_menu']

    def __str__(self):
        return self.cake_name
