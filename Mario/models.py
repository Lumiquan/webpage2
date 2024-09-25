from django.db import models

class NewProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    about = models.TextField(blank=True, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    country = models.CharField(max_length=100)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)

    def __str__(self):
        return self.username
