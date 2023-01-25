from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

CAKE_SELECTIONS = (0, "white chocolate / chocolate cakes"), (1, "cream cakes / jam cakes")
(2, "fruit & nut cakes"), (3, "sponges")


# cake item moduels
class CakeItem(models.Model):
    cake_id = models.AutoField(primary_key=True)
    cake_name = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=200, unique=True)
    dietary = models.CharField(max_length=200)
    allergens = models.CharField(max_length=200, null=True)
    featured_image = CloudinaryField('image', default='placeholder')
    on_menu = models.BooleanField(default=False)
    updated_on = models.DateTimeField(auto_now=True)


class Meta:
    ordering = ['-on_menu']

    def __str__(self):
        return self.cake_name
