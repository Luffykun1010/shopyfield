from django.db import models
from django.contrib.auth.models import User
class Main_Categories(models.Model):
    cat_name=models.CharField(max_length=200)
    cat_img=models.ImageField(upload_to='Categories')
    category_code=models.CharField(max_length=200)
    def __str__(self):
        return self.category_code
class Categories(models.Model):
    main_category=models.ForeignKey(Main_Categories,on_delete=models.CASCADE)
    sub_cat_name=models.CharField(max_length=200)
    sub_category_code=models.CharField(max_length=200)
    def __str__(self):
        return self.sub_category_code

class Products(models.Model):
    cat_name=models.ForeignKey(Categories,on_delete=models.CASCADE)
    prd_name=models.CharField(max_length=200)
    prd_img=models.ImageField(upload_to='Categories')
    prd_size=models.CharField(max_length=200)
    prd_rate=models.IntegerField()
    prd_quantity=models.IntegerField()
    prd_desc=models.CharField(max_length=500)
    seller_company=models.CharField(max_length=200)
    product_code=models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    total_sale=models.IntegerField()
    def __str__(self):
        return self.prd_name
    class Meta:
        ordering = ['-created_at',]

class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    order_qty=models.CharField(max_length=200)
    def __str__(self):
        return self.user.username

class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    user_name=models.CharField(max_length=200)
    user_contact=models.CharField(max_length=10)
    user_housename=models.CharField(max_length=200)
    user_roadname=models.CharField(max_length=200)
    user_pincode=models.CharField(max_length=200)
    user_state=models.CharField(max_length=200)
    user_city=models.CharField(max_length=200)
    def __str__(self):
        return self.user_housename

class Payment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    payment_method=models.CharField(max_length=200)
    def __str__(self):
        return self.payment_method

class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.ForeignKey(Address,on_delete=models.CASCADE)
    rate=models.CharField(max_length=200)
    trackingid=models.CharField(max_length=200)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    prd_rate=models.CharField(max_length=200)
    prd_qty=models.CharField(max_length=200)
    createdat=models.DateField(auto_now_add=True)
    def __str__(self):
        return self.trackingid