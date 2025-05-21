from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ProductCategory(models.Model):
    pcategory = models.CharField(max_length=100)

    def __str__(self):
        return self.pcategory

class Products(models.Model):
    pname = models.CharField(max_length=100)
    pdesc = models.CharField(max_length=250)
    price = models.IntegerField(default=0)
    ProductCategory = models.ManyToManyField(ProductCategory)
    pimages = models.ImageField('Default.jpg',upload_to='uploads')
    Trending = models.BooleanField(default=False)
    Offer = models.BooleanField(default=False)

    def __str__(self):
        return self.pname


class CartModel(models.Model):
    pname=models.CharField(max_length=100)
    price=models.IntegerField(default=0)
    pcategory=models.ManyToManyField(ProductCategory)
    quantity=models.IntegerField(default=0)
    totalprice=models.IntegerField(default=0)
    host=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.pname