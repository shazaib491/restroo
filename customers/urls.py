from django.urls import path
from .views import *

urlpatterns = [
    path('reserve',reserve, name='reserve'),
    path('shop_cart',shop_cart,name="shopCart"),
    path('cartDelete/<int:Oid>',cartDelete,name="cartDelete")
]
