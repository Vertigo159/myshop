from django.shortcuts import render

def home_page(request):
    return render(request, "home.html",{})

def shop_page(request):
    return render(request, "shop.html",{})

def cart_page(request):
    return render(request, "cart.html",{})

def checkout_page(request):
    return render(request, "checkout.html",{})

def single_page(request):
    return render(request, "single.html",{})