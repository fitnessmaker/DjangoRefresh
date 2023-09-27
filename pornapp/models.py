from django.db import models
#superuser nasarudheensha ps: 99**44
# Create your models here.


#Team Start sectino in index.html
class Members(models.Model):

    photo = models.ImageField(upload_to='photos')
    name = models.CharField(max_length=100)
    desc = models.TextField()
    salary = models.IntegerField()


class Appartment(models.Model):

    av = models.BooleanField(default=False)
    pics = models.ImageField(upload_to='Gallery')
    types = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    des = models.TextField()





