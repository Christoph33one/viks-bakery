from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    not_read = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        # returns full name
        return self.name
