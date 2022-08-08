from django.db import models
from django.contrib.auth.models import AbstractUser

from phonenumber_field.modelfields import PhoneNumberField

class User(AbstractUser):
    is_customer = models.BooleanField(default = False)
    is_salesman = models.BooleanField(default = False)
    is_admin = models.BooleanField(default  = False)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name='customer', blank = True, null = True)
    full_name = models.CharField(max_length = 100)
    contact_no = PhoneNumberField()
    address = models.CharField(max_length = 200)

    def __str__(self):
        return self.full_name

class Salesman(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'salesman', blank= True, null = True)
    full_name = models.CharField(max_length = 100)
    contact_no = PhoneNumberField()
    address = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.full_name

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, related_name = 'admin', blank = True, null = True)
    full_name = models.CharField(max_length = 100)
    contact_no = PhoneNumberField()
    address = models.CharField(max_length = 200)

    def __str__(self):
        return self.full_name