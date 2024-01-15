from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Company
# from shopyfield_home.models import Products,Orders
def sellers_home(request):
    user=request.user
    company=Company.objects.filter(user=user)
    if company:
        for i in company:
            products=Products.objects.filter(seller_company=i.company_name)
    else:
        return redirect('home')
    order=Orders.objects.all()
    return render(request,'sellerspage/home.html',{'company':company})
def sellers_prd(request):
    user=request.user
    company=Company.objects.filter(user=user)
    for i in company:
        products=Products.objects.filter(seller_company=i.company_name)
    return render(request,'sellerspage/products.html',{'products':products})
def sellers_prddetails(request,product_code):
    products=Products.objects.filter(product_code=product_code)
    product_name=Products.objects.filter(product_code=product_code).first()
    if request.method == 'POST':
        prd_code=request.POST.get('prd_code')
        products=Products.objects.get(product_code=prd_code)
        products.prd_name=request.POST.get('prd_name')
        products.save()
        return redirect('sellers_prd')
    return render(request,'sellerspage/prddetails.html',{'products':products,'product_name':product_name})
def sellers_orders(request):
    order=Orders.objects.all()
    user=request.user
    company=Company.objects.filter(user=user)
    return render(request,'sellerspage/orders.html',{'order':order,'company':company,})