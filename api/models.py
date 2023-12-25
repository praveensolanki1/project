from django.db import models
from django.urls import reverse

# Create your models here.


class UserProfile(models.Model):
    schooling = models.CharField(max_length=500)
    achievements  = models.CharField(max_length=400)
class Item(models.Model):
    category = models.CharField(max_length=255)
    subcategory = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    slug =  models.SlugField(max_length=50,default="",null=False)
   

    def __str__(self):
        return self.name


    def get_absolute_url(self):
        return reverse('api:index')    

class Auth(models.Model):
    name= models.CharField(max_length=255)
    age = models.IntegerField()
    def __str__(self):
        return self.name