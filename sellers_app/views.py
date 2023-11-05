from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Company
from shopyfield_home.models import Products,Orders
def sellers_home(request):
    user=request.user
    company=Company.objects.filter(user=user)
    if company:
        for i in company:
            products=Products.objects.filter(seller_company=i.company_name)
    else:
        return redirect('home')
    order=Orders.objects.all()
    return render(request,'sellerspage/home.html',{'company':company,'products':products,'order':order})