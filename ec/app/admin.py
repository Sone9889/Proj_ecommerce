from django.contrib import admin
from . models import Product

# Register your models here.

@admin.register(Product)
class ProductModleAdmin(admin.ModelAdmin):
    list_display = ['id','discounted_price','category','product_image']