from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product", views.prod, name="prod"),
    path("product/<int:id>", views.view_product, name="view_product"),
    path("akchuya", views.akchuya, name="akchuya"),
]