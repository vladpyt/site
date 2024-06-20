from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<img src='https://sdnem-rozhdeniya.ru/_ph/47/542611427.jpg'>")