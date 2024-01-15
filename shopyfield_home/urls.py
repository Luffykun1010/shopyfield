from . import views
from django.contrib.auth import views as auth_views
from django.urls import path,include
urlpatterns = [
    path('',views.home,name='home'),
    path('home',views.home,name='home'),
    path('Category',views.categorypage,name='category'),
    path('Category/<str:category_code>',views.subcat,name='subcat'),
    path('category/<str:category_code>/<str:sub_category_code>',views.pdtfltr,name='pdtfltr'),
    path('category/<str:category_code>/<str:sub_category_code>/<str:product_code>',views.pdtdtls,name='pdtdtls'),
    path('signup',views.signup,name='signup'),
    path('login',views.loginpage,name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    path('cart',views.cart,name='cart'),
    path('delcart',views.delcart,name='delcart'),
    path('orders',views.orders,name='orders'),
    path('delorder/<str:trackingid>',views.delorder,name='delorder'),
    path('address',views.address,name='address'),
    path('change-address',views.chaddress,name='chaddress'),
    path('payment',views.payment,name='payment'),
    path('change-payment',views.chpayment,name='chpayment'),
    path('booking',views.booking,name='booking'),
]