from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
import random
from django.contrib.auth import authenticate,login,logout
from .models import Categories,Products,Cart,Address,Payment,Orders,Orderitems
cartcount=Cart.objects.all().count
def home(request):
    dict_cate={
        'cartcount':cartcount,
        'cat':Categories.objects.all()
    }
    return render(request,'homepage/home.html',dict_cate)
def pdtfltr(request,category_code):
    if(Categories.objects.filter(category_code=category_code)):
        products=Products.objects.filter(category_code=category_code)
        category_name=Categories.objects.filter(category_code=category_code).first()
        context={'products':products,'category_name':category_name,'cat':Categories.objects.all(),'cartcount':cartcount}
        return render(request,'homepage/products.html',context)
def pdtdtls(request,category_code,product_code):
    if(Categories.objects.filter(category_code=category_code)):
        if(Products.objects.filter(product_code=product_code)):
            products=Products.objects.filter(product_code=product_code)
            category_name=Categories.objects.filter(category_code=category_code).first()
            product_name=Products.objects.filter(product_code=product_code).first()
            if request.method == 'POST':
                if request.user.is_authenticated:
                    product_id=request.POST.get('prd_id')
                    user=request.user 
                    order_qty=request.POST.get('order_qty')
                    if(Cart.objects.filter(user=request.user.id,product_id=product_id)):
                        messages.error(request,"Already added to cart")  
                    else:
                        for d in products:
                            if d.prd_quantity < int(order_qty):
                                messages.error(request,"Order quantity should be below stock quantity.")  
                            else:
                                carts=Cart.objects.create(user=user,order_qty=order_qty,product_id=product_id)
                                carts.save()
                                return redirect('cart')
                else:
                    return redirect('login')
            prod={'products':products,'category_name':category_name,'product_name':product_name,'cat':Categories.objects.all(),'cartcount':cartcount}
    return render(request,'homepage/productdetails.html',prod)
def signup(request):
    if request.method == 'POST':
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myuser=User.objects.create_user(phone,email,password)
        myuser.save()
        return redirect('login')
    return render(request,'homepage/signup.html')
def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('phone')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:    
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('login')
    return render(request,'homepage/login.html')
def logoutpage(request):
    logout(request)
    return redirect('home')
def categorypage(request):
    catcount=Categories.objects.all().count
    dict_cate={
        'cat':Categories.objects.all(),
        'catcount':catcount,
        'cartcount':cartcount
    }
    return render(request,'homepage/category.html',dict_cate)
def cart(request):
    cart=Cart.objects.filter(user=request.user)
    totalrate = 0
    totalquantity = 0
    for i in cart:
        totalquantity=int(i.order_qty)+totalquantity
        totalrate=(int(i.order_qty)*int(i.product.prd_rate)+totalrate)
    if request.method == 'POST':
        product_id=request.POST.get('prd_id')
        if(Cart.objects.filter(user=request.user,product_id=product_id)):
            order_qty=int(request.POST.get('order_qty'))
            cart=Cart.objects.get(user=request.user,product_id=product_id)
            cart.order_qty=order_qty
            cart.save()
            return redirect('cart')
    dict_cart={
        'totalquantity':totalquantity,
        'totalrate':totalrate,
        'cart':cart,
        'cartcount':cartcount,
        'cat':Categories.objects.all()
    }
    return render(request,'homepage/cart.html',dict_cart)
def delcart(request):
    product_id=request.POST.get('prd_id')
    if(Cart.objects.filter(product_id=product_id)):
        cart=Cart.objects.filter(product_id=product_id)
        if request.method == 'POST':
            cart.delete()
            return redirect('cart')
def booking(request):
    cart=Cart.objects.filter(user=request.user)
    totalrate = 0
    totalquantity = 0
    for i in cart:
        totalquantity=int(i.order_qty)+totalquantity
        totalrate=(int(i.order_qty)*int(i.product.prd_rate)+totalrate)
    address=Address.objects.filter(user=request.user)
    payment=Payment.objects.filter(user=request.user)
    dict_book={
        'totalquantity':totalquantity,
        'totalrate':totalrate,
        'cart':cart,
        'cartcount':cartcount,
        'payment':payment,
        'address':address,
        'cat':Categories.objects.all()
    }
    return render(request,'homepage/booking.html',dict_book)
def address(request):
    if request.method == 'POST':
        user=request.user
        user_name=request.POST.get('usersname')
        user_contact=request.POST.get('usersphone')
        user_housename=request.POST.get('usershouse')
        user_roadname=request.POST.get('usersarea')
        user_pincode=request.POST.get('userspincode')
        user_state=request.POST.get('usersstate')
        user_city=request.POST.get('userscity')
        address=Address.objects.create(user=user,user_name=user_name,user_contact=user_contact,user_housename=user_housename,user_roadname=user_roadname,user_pincode=user_pincode,user_state=user_state,user_city=user_city)
        address.save()
        return redirect('booking')
def chaddress(request):
    address=Address.objects.filter(user=request.user)
    dict_book={
        'address':address,
        'cartcount':cartcount,
        'cat':Categories.objects.all()
    }
    if request.method == 'POST':
        address=Address.objects.get(user=request.user)
        address.user=request.user
        address.user_name=request.POST.get('usersname')
        address.user_contact=request.POST.get('usersphone')
        address.user_housename=request.POST.get('usershouse')
        address.user_roadname=request.POST.get('usersarea')
        address.user_pincode=request.POST.get('userspincode')
        address.user_state=request.POST.get('usersstate')
        address.user_city=request.POST.get('userscity')
        address.save()
        return redirect('booking')
    return render(request,'homepage/changeaddress.html',dict_book)
def payment(request):
    if request.method == 'POST':
        user=request.user
        payment_method=request.POST.get('payment')
        payment=Payment.objects.create(user=user,payment_method=payment_method)
        payment.save()
        return redirect('booking')
def chpayment(request):
    payment=Payment.objects.get(user=request.user)
    payment.delete()
    return redirect('booking')
def orders(request):
    if request.method == 'POST':
        user=request.user
        cart=Cart.objects.filter(user=request.user)
        address=Address.objects.get(user=request.user)
        totalrate = 0
        for i in cart:
            totalrate=(int(i.order_qty)*int(i.product.prd_rate)+totalrate)
            product=i.product
            prd_rate=i.product.prd_rate
            prd_qty=i.order_qty
        trackingid=str(random.randint(111111,999999))
        while Orders.objects.filter(user=user):
            trackingid=str(random.randint(111111,999999))
        neworder=Orders.objects.create(user=user,address=address,rate=totalrate,trackingid=trackingid)
        neworder.save()
        cart=Cart.objects.filter(user=request.user)
        for i in cart:
            orderitem=Orderitems.objects.create( orders=neworder,product=product,prd_rate=prd_rate,prd_qty=prd_qty)
            orderitem.save()
            orderproduct=Products.objects.filter(id=i.product_id).first()
            orderproduct.prd_quantity=int(orderproduct.prd_quantity)-int(i.order_qty)
            orderproduct.save()
        cart.delete()
    orders=Orders.objects.filter(user=request.user)
    context={'orders':orders,'cat':Categories.objects.all(),'cartcount':cartcount}
    return render(request,'homepage/order.html',context)
def delorder(request,trackingid):
    if(Orders.objects.filter(trackingid=trackingid)):
        orders=Orders.objects.filter(trackingid=trackingid)
        context={'orders':orders,'cat':Categories.objects.all(),'cartcount':cartcount}
        if request.method == 'POST':
            orderitem=Orderitems.objects.filter(orders=orders)
            # for i in orders:
            #     orderproduct=Products.objects.filter(id=i.product_id).first()
            #     orderproduct.prd_quantity=int(orderproduct.prd_quantity)+int(i.prd_qty)
            #     orderproduct.save()
            orders.delete() 
            return redirect('orders')
        return render(request,'homepage/delorder.html',context)
        