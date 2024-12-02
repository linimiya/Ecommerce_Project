from django.db import models


class Contact_DB(models.Model):
    Contact_Name = models.CharField(max_length=100, blank=True, null=True)
    Contact_Email = models.CharField(max_length=100, blank=True, null=True)
    Contact_TextArea = models.TextField(max_length=100, blank=True, null=True)


class Signup_DB(models.Model):
    Sigin_Name = models.CharField(max_length=100, blank=True, null=True)
    Sigin_Email = models.CharField(max_length=100, blank=True, null=True)
    Sigin_Mobile = models.IntegerField(blank=True, null=True)
    Sigin_Pswd = models.CharField(max_length=100, blank=True, null=True)
    Sigin_confpswd = models.CharField(max_length=100, blank=True, null=True)


class Cart_DB(models.Model):
    No_of_orders = models.IntegerField(blank=True, null=True)
    Price_Per_Quantity = models.CharField(max_length=100, blank=True, null=True)
    Total_price = models.IntegerField(blank=True, null=True)
    Product_Name = models.CharField(max_length=100, blank=True, null=True)
    Sigin_Name = models.CharField(max_length=100, blank=True, null=True)
    Prod_Img = models.ImageField(upload_to="Cart_Images", blank=True, null=True)


class Order_DB(models.Model):
    Name = models.CharField(max_length=100, blank=True, null=True)
    Email = models.CharField(max_length=100, blank=True, null=True)
    Place = models.CharField(max_length=100, blank=True, null=True)
    Address = models.CharField(max_length=100, blank=True, null=True)
    Mobile = models.IntegerField(blank=True, null=True)
    Message = models.TextField(max_length=100, blank=True, null=True)
    Sub_Total = models.IntegerField(blank=True, null=True)
    Shipping_Price = models.IntegerField(blank=True, null=True)
    Final_Pay = models.IntegerField(blank=True, null=True)
# Create your models here.
