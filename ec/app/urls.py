from django.contrib import admin
from django.urls import path
from .views import CategoryView, home, ProductDetail, CategoryTitle , AboutView # Import the `home` view
from django.conf import settings
from django.conf.urls.static import static
from . import views

# URL patterns เริ่มต้น
urlpatterns = [
    # ตั้งค่าเส้นทาง URL ที่เรียกการทำงานของ view `home`
    path('', home, name='home'), 
    
    # About
    path('about/', AboutView.as_view(), name='about'),

    # Contact
    path('contact/', views.contact,name="contact"),

    # ตั้งค่าเส้นทาง URL สำหรับหน้า admin ของ Django
    path('admin/', admin.site.urls),
    
    # ตั้งค่าเส้นทาง URL สำหรับแสดงสินค้าตามหมวดหมู่โดยใช้ `CategoryView`
    path('category/<slug:val>/', views.CategoryView.as_view(), name='category'),
    
    # ตั้งค่าเส้นทาง URL สำหรับแสดงสินค้าที่มี title โดยใช้ `CategoryView`
    path('category-title/<str:val>/', CategoryTitle.as_view(), name='category-title'),    
    # ตั้งค่าเส้นทาง URL สำหรับหน้ารายละเอียดสินค้าโดยใช้ `ProductDetail`
    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    # login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
]

# สำหรับการใช้ไฟล์รูปหรือสื่ออื่นๆ ในระหว่างการพัฒนา (DEBUG mode)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
