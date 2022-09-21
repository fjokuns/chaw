from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import User
from techbro.models import Dish
# Create your models here.


['user', 'dish', 'c_name', 'quantity']
class Shopcart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    c_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    c_price = models.IntegerField()
    amount = models.IntegerField()
    cart_code = models.CharField(max_length=255, default='a')
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    
    class Meta:
        db_table = 'Shopcart'
        managed = True
        verbose_name = 'Shopcart'
        verbose_name_plural = 'Shopcart'


class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    first_name = models.CharField(max_length=50, editable=False)
    last_name = models.CharField(max_length=50, editable=False)
    total = models.IntegerField(editable=False)
    cart_code= models.CharField(max_length=225, editable=False)
    pay_code = models.CharField(max_length=36, editable=False)
    paid = models.BooleanField(default=False, editable=False)
    pay_date = models.DateTimeField(auto_now_add=True)
    admin_note = models.CharField(max_length=225)
    admin_update = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=20, default='a')
    address = models.CharField(max_length=500, default='Lagos')
    city = models.CharField(max_length=225 ,default='Lagos')

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'payment'
        managed = True
        verbose_name = 'Payment'
        verbose_name_plural = 'Payments'