from django.urls import path

from dashboard import views

app_name = 'dashboard'

urlpatterns = [
    path('products/', views.index, name='products'),
    path('products/create', views.create, name='create_product'),
    path('products/store', views.store, name='detail_product'),
    path('products/update/<str:id>', views.edit, name='update_product'),
    path('products/delete/<str:id>/', views.delete, name='delete_product'),
    
    path('categories/', views.index_categories, name='categories'),
    path('categories/create', views.create_categories, name='create_categories'),
    path('categories/store_categories', views.store_categories, name='store_categories'),
    path('categories/update/<str:id>', views.edit_categories, name='update_categories'),
    path('categories/delete/<str:id>/', views.delete_categories, name='delete_categories'),  
]
