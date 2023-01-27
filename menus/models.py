from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# CAKE_SELECTIONS = (
#     (0, "white"),
#     (1, "fruit"),
#     (2, "New item"),
# )

CAKE_SELECTIONS = ((0, "Chocolate Cakes"), (1, "Cream cakes"), (2, "New item"))


# cake item moduels
class CakeItem(models.Model):
    """model for admin cake list"""
    cake_id = models.AutoField(primary_key=True)
    cake_name = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=200, unique=True)
    dietary = models.CharField(max_length=200)
    allergens = models.CharField(max_length=200, null=True)
    cake_selections = models.IntegerField(
        choices=CAKE_SELECTIONS, default=2)
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
# ask if you should build a seperate module in a new app for the request form
# look at modules for a drop down menu. (for nav bar / menu)
# look at a module for a user views
