from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib import messages
import random
from django.contrib.auth import authenticate,login,logout
from .models import Main_Categories,Categories,Products,Cart,Address,Payment,Orders
from django.http import JsonResponse
def home(request):
    latest_nike=Products.objects.filter(seller_company="nike").first()
    dict_cate={
        'main_cat':Main_Categories.objects.all(),
        'cat':Categories.objects.all(),
        'prd':Products.objects.all()[:4],
        'recent':Products.objects.all().order_by('-total_sale')[:4],
        'latest':latest_nike
    }
    return render(request,'homepage/home.html',dict_cate)
def categorypage(request):
    dict_cate={
        'main_cat':Main_Categories.objects.all()
    }
    return render(request,'homepage/category.html',dict_cate)
def subcat(request,category_code):
    if(Main_Categories.objects.filter(category_code=category_code)):
        main_cats=Main_Categories.objects.filter(category_code=category_code).first()
        categories=Categories.objects.filter(main_category=main_cats)
        dict_cate={
            'cats':categories,
            'main_cat':Main_Categories.objects.all(),
            'cat':Categories.objects.all(),
            'main_cats':main_cats
        }
        return render(request,'homepage/category_sub.html',dict_cate)
def pdtfltr(request,category_code,sub_category_code):
    if(Main_Categories.objects.filter(category_code=category_code)):
        main_cats=Main_Categories.objects.filter(category_code=category_code).first()
        categories=Categories.objects.filter(sub_category_code=sub_category_code).first()
        products=Products.objects.filter(cat_name=categories)
        context={'products':products,'main_cat':Main_Categories.objects.all(),'main_cats':main_cats,'cats':categories,'cat':Categories.objects.all()}
        return render(request,'homepage/products.html',context)
def pdtdtls(request,category_code,sub_category_code,product_code):
    if(Main_Categories.objects.filter(category_code=category_code)):
            prd=Products.objects.filter(product_code=product_code)
            product=Products.objects.filter(product_code=product_code).first()
            main_cats=Main_Categories.objects.filter(category_code=category_code).first()
            cates=Categories.objects.filter(sub_category_code=sub_category_code).first()
            if request.method == 'POST':
                if request.user.is_authenticated:
                    product_id=request.POST.get('prd_id')
                    user=request.user 
                    order_qty=request.POST.get('order_qty')
                    if(Cart.objects.filter(user=request.user.id,product_id=product_id)):
                        messages.error(request,"Already added to cart")  
                    else:
                        for d in prd:
                            if d.prd_quantity < int(order_qty):
                                messages.error(request,"Order quantity should be below stock quantity.")  
                            else:
                                carts=Cart.objects.create(user=user,order_qty=order_qty,product_id=product_id)
                                carts.save()
                                return redirect('cart')
                else:
                    return redirect('login')
            return render(request,'homepage/productdetails.html',{'cat':Categories.objects.all(),'products':prd,'product':product,'main_cat':Main_Categories.objects.all(),'main_cats':main_cats,'cats':cates})
def signup(request):
    if request.method == 'POST':
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        myuser=User.objects.create_user(phone,email,password)
        myuser.save()
        return redirect('login')
    return render(request,'homepage/signup.html',{'main_cat':Main_Categories.objects.all()})
def loginpage(request):
    if request.method == 'POST':
        username=request.POST.get('phone')
        password=request.POST.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:    
            login(request,user)
            return redirect('cart')
        else:
            messages.error(request,"Invalid credentials")
            return redirect('login')
    return render(request,'homepage/login.html',{'main_cat':Main_Categories.objects.all(),'cat':Categories.objects.all(),})
def logoutpage(request):
    logout(request)
    return redirect('home')
def cart(request):
    if request.user.is_authenticated:
        cart=Cart.objects.filter(user=request.user)
        cart_1=Cart.objects.filter(user=request.user).first()
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
    else:
        return redirect('login')
    dict_cart={
        'totalquantity':totalquantity,
        'totalrate':totalrate,
        'cart':cart,
        'main_cat':Main_Categories.objects.all()
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
    booking_rate = 0
    booking_quantity = 0
    delivery_charge=50
    for i in cart:
        booking_quantity+=int(i.order_qty)
        booking_rate+=int(i.product.prd_rate)
    totalrate=delivery_charge+(booking_rate*booking_quantity)
    address=Address.objects.filter(user=request.user)
    payment=Payment.objects.filter(user=request.user)
    dict_book={
        'booking_quantity':booking_quantity,
        'booking_rate':booking_rate,
        'cart':cart,
        'payment':payment,
        'address':address,
        'totalrate':totalrate,
        'delivery_charge':delivery_charge,        
        'main_cat':Main_Categories.objects.all(),
        'cat':Categories.objects.all(),
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
    if(address):
        if request.method == 'POST':
            address.delete()
            return redirect('booking')
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
            while Orders.objects.filter(trackingid=trackingid):
                trackingid=str(random.randint(111111,999999))
            neworder=Orders.objects.create(user=user,address=address,rate=totalrate,trackingid=trackingid,product=product,prd_rate=prd_rate,prd_qty=prd_qty)
            neworder.save()
        cart=Cart.objects.filter(user=request.user)
        for i in cart:
            orderproduct=Products.objects.filter(id=i.product_id).first()
            orderproduct.prd_quantity=int(orderproduct.prd_quantity)-int(i.order_qty)
            orderproduct.save()
        cart.delete()
    orders=Orders.objects.filter(user=request.user)
    order_frt=Orders.objects.filter(user=request.user).first()
    context={'cat':Categories.objects.all(),'orders':orders,'cat':Categories.objects.all(),'order_frt':order_frt,'main_cat':Main_Categories.objects.all(),}
    return render(request,'homepage/order.html',context)
def delorder(request,trackingid):
    if(Orders.objects.filter(trackingid=trackingid)):
        orders=Orders.objects.filter(trackingid=trackingid)
        context={'orders':orders,'cat':Categories.objects.all()}
        if request.method == 'POST':
            orders=Orders.objects.filter(trackingid=trackingid)
            for i in orders:
                orderproduct=Products.objects.filter(id=i.product_id).first()
                orderproduct.prd_quantity=int(orderproduct.prd_quantity)-int(i.prd_qty)
                orderproduct.save()
                orders.delete() 
            return redirect('orders')
        return render(request,'homepage/delorder.html',context)
    