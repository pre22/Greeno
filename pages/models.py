from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(max_length=40)
    phone = models.IntegerField()
    message = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    