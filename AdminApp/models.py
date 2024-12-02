from django.db import models


class Catgory_DB(models.Model):
    Category_Name = models.CharField(max_length=100, blank=True, null=True)
    Category_Image1 = models.ImageField(upload_to="SareePic", blank=True, null=True)
    Category_Image2 = models.ImageField(upload_to="SareePic", blank=True, null=True)
    Category_Image3 = models.ImageField(upload_to="SareePic", blank=True, null=True)


class Product_DB(models.Model):
    Category_of_Product = models.CharField(max_length=100, blank=True, null=True)
    Product_Name = models.CharField(max_length=100, blank=True, null=True)
    Product_Image1 = models.ImageField(upload_to="SareePic", blank=True, null=True)
    Product_Image2 = models.ImageField(upload_to="SareePic", blank=True, null=True)
    Product_Image3 = models.ImageField(upload_to="SareePic", blank=True, null=True)
    Product_Price=models.IntegerField(blank=True, null=True)
# Create your models here.
