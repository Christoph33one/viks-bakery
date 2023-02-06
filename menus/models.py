from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# list for chocolate cakes items in database
CAKE_SELECTIONS = (
    (0, "Chocolate Cakes"),
    (1, "Vegan Cakes"),
    (2, "New item"))

# list for cream cake items in database
CREAM_CAKE_SELECTIONS = (
    (0, "Cream Cakes"),
    (1, "Vegan Cakes"),
    (2, "New item")
    )

# list of cheese cake items in the database
CHEESE_CAKE_SELECTIONS = {
    (0, "Cheese Cakes"),
    (1, "Vegan Cakes"),
    (2, "New item")
}


# choclate cake module
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


# cream cake module
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


# cheese cakes module
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


# check user login and details are in the admin panel
# create a user module !!
# look at user module templates on github!
# look at modules for a drop down menu. (for nav bar / menu)
# look at a module for a user views