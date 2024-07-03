from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    products = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    return render(request, "index.html", {
        'products': products
    })