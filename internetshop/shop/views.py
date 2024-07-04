from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    '''products = Product.objects.all()'''
    return render(request, "home_page.html")

def prod(request):
    products = Product.objects.all()
    return render(request, "index.html", {
        'products': products
    })

def view_product(request, id):
    product = Product.objects.filter(id=id).first()
    review = product.review_set.all()

    return render(request, "product.html", {
        'product': product,
        'review': review
    })

def akchuya(request):
    return render(request, "akchuya.html")