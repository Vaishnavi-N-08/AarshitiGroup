from django.contrib import admin

from spices.models import Cart, CartItem, Product

# Register your models here.

class ProductModelAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'price',
        'description',
        
    ]

    class Meta:
        model = Product

class CartModelAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'date_added',
        'address',
        'phone',
            ]

    class Meta:
        model = Cart


class CartItemModelAdmin(admin.ModelAdmin):
    list_display = [
        'cart',
        'product',
        'quantity',
        'date_added'
        
    ]

    class Meta:
        model = CartItem



admin.site.register(Product, ProductModelAdmin)
admin.site.register(Cart, CartModelAdmin)
admin.site.register(CartItem, CartItemModelAdmin)
