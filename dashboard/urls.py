from django.urls import path

from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('products/', views.index, name='products'),
    path('products/create', views.create, name='create_product'),
    path('products/store', views.store, name='detail_product'),
    path('products/update/<str:id>', views.edit, name='update_product'),
    path('products/delete/<str:id>/', views.delete, name='delete_product'),
    
]
