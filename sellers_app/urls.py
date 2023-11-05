from . import views
from django.contrib.auth import views as auth_views
from django.urls import path,include
urlpatterns = [
    path('sellers_home',views.sellers_home,name='sellers_home'),
]