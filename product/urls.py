from django.urls import path

from product import views

app_name = 'products'

urlpatterns = [
    path('', views.show_products, name='productss'),
]
