from django.contrib import admin
from django.contrib import admin
from .models import Categories,Products,Cart,Address,Payment,Orders,Orderitems

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Payment)
admin.site.register(Orders)
admin.site.register(Orderitems)