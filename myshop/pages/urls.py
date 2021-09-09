from django.urls import path
from pages.views import *

urlpatterns = [
    path("", home_page, name="home_page"),
    path("shop", shop_page, name="shop_page"),
    path("cart", cart_page, name="cart_page"),
    path("checkout", checkout_page, name="checkout_page"),
    path("single", single_page, name="single_page")
]
