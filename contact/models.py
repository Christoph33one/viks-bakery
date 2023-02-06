from django.db import models


# create models here
class Customer(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        # returns full name
        return self.full_name
