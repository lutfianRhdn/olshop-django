from django.urls import path

from product import views

app_name = 'product'

urlpatterns = [
    path('', views.show_products, name='products'),
    path('get-all-calendar-event',views.get_all_calendar_event, name="get-all-calendar-event"),
    path('<str:kode>/',views.product_detail,name="detail")
]
