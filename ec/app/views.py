from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views import View
from .models import Product
from django.db.models import Count
from . forms import CustomerRegistrationForm

# สร้างฟังก์ชันหน้าหลัก
def home(request: HttpRequest) -> HttpResponse:
    # แสดงหน้าโฮมเพจ (home.html)
    return render(request, "app/home.html")

# About
class AboutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        # สมมติว่าคุณต้องการดึง product ด้วย pk = 1
        product = get_object_or_404(Product, pk=1)
        return render(request, "app/about.html", {"product": product})






# Contect
def contact(request):
    return render(request,"app/contact.html")
# คลาส CategoryView เพื่อแสดงสินค้าตามหมวดหมู่
class CategoryView(View):
    def get(self, request: HttpRequest, val: str) -> HttpResponse:
        # กรองสินค้าตามหมวดหมู่ที่กำหนด
        products = Product.objects.filter(category=val)
        
        if products.exists():
            # ถ้ามีสินค้าในหมวดหมู่นี้, ส่งค่า title และ pk ไป
            titles = products.values('title', 'pk')
        else:
            # ถ้าไม่มีสินค้าในหมวดหมู่นี้, ส่งรายการเป็นค่าว่าง
            titles = []

        # แสดงหน้า category.html พร้อมกับส่งข้อมูลสินค้าที่กรองได้
        return render(request, "app/category.html", {"products": products, "titles": titles, "category": val})



# แก้ไขการตั้งชื่อ และแก้ไขข้อผิดพลาดใน CategoryTitle
class CategoryTitle(View):
    def get(self, request: HttpRequest, val: str) -> HttpResponse:
        # กรองสินค้าตามชื่อ
        products = Product.objects.filter(title=val)
        
        if products.exists():
            category = products[0].category
            titles = Product.objects.filter(category=category).values('title')
        else:
            titles = []

        # แสดงหน้า category.html พร้อมกับส่งข้อมูลที่กรองได้
        return render(request, "app/category.html", {"products": products, "titles": titles, "category": category})



# คลาส ProductDetail เพื่อแสดงรายละเอียดสินค้าตาม primary key (pk)
class ProductDetail(View):
    def get(self, request: HttpRequest, pk: int) -> HttpResponse:
        # ดึงข้อมูลสินค้าจากฐานข้อมูลตาม pk, ถ้าไม่พบจะแสดง 404
        product = get_object_or_404(Product, pk=pk)
        
        # แสดงหน้า productdetail.html พร้อมข้อมูลสินค้าที่ดึงได้
        return render(request, "app/productdetail.html", {"product": product})
 

class CustomerRegistrationView(View):
    def get(self,request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html', locals())