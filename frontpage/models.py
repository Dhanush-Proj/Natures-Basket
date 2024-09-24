from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=255)
    phone_no = models.CharField(max_length=255)
    email_addr = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    state_f = models.enums
    
