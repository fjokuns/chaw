from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('contact',contact, name='kontact'),
    path('category',category, name='category'),
    path('all_food',all_food, name='all_food'),
    path('singlecat/<str:id>',singlecat,name='singlecat'),
    path('detail/<str:id>',detail, name='detail'),
    path('signin', signin, name='signin'),
    path('register',signup, name='register'),
    path('signout', signout, name='signout'),
    # path('signout', signup, name='register')
    path('profile', profile, name='profile'),
    path('profileupdate', profileupdate, name='profileupdate'),
    path('passwordupdate', passwordupdate, name='passwordupdate'),
    path('ordermeal', ordermeal, name='ordermeal'),
    path('mycart', mycart, name='mycart'),
    path('decrease', decrease, name='decrease'),
    path('increase', increase, name='increase'),
    path('deletemeal', deletemeal, name='deletemeal'),
    path('deleteallmeal', deleteallmeal, name='deleteallmeal'),
    path('checkout', checkout, name='checkout'),
    path('payment', payment, name='payment'),
    path('completed', completed, name='completed'),
]
