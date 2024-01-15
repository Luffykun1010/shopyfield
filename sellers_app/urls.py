from . import views
from django.contrib.auth import views as auth_views
from django.urls import path,include
urlpatterns = [
    path('sellers_home',views.sellers_home,name='sellers_home'),
    path('sellers_products',views.sellers_prd,name='sellers_prd'),
    path('sellers_products/<str:product_code>',views.sellers_prddetails,name='sellers_prddetails'),
    path('sellers_orders',views.sellers_orders,name='sellers_orders'),
]