from django.contrib import admin
from .models import Customer, OrderPlaced, Payment,Product, Cart, Wishlist
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
   list_display = ['id','title','discounted_price','category','product_image']

@admin.register(Customer)
class ProductModelAdmin(admin.ModelAdmin):
   list_display = ['id', 'user', 'locality', 'city', 'state', 'zipcode']
   def product(self,obj):
      link = reverse("admin:app_product_change",args=[obj.product.pk])
      return format_html('<a href="{}"></a>',link, obj.product.title)

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
   list_display = ['id', 'user', 'product', 'quantity']

@admin.register(Payment)
class PaymentModelAdmin(admin.ModelAdmin):
   list_display = ['id','user','amount','paid']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
   list_display=['id', 'user','customer', 'product', 'quantity', 'ordered_date','status','payment']

@admin.register(Wishlist)
class WishlistModelAdmin(admin.ModelAdmin):
   list_display = ['id','user','product']