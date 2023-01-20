from datetime import date
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    date_birth = models.DateField(default=date.today())
    email = models.EmailField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField(default='avatar.png', blank=True, null=True)
    phone = models.IntegerField(max_length=15)
    insta = models.CharField(max_length=50)
    github = models.CharField(max_length=50)
    order_count = models.PositiveIntegerField(default=0)
    wallet = models.PositiveIntegerField(default=0)


    def __str__(self):
        return f"{self.full_name}"