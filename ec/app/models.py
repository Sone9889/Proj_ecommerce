from django.db import models

# กำหนดตัวเลือกประเภทสินค้า
CATEGOTY_CHOICES = (
    ('CR', 'Curd'),
    ('ML', 'Milk'),
    ('LS', 'Lassi'),
    ('MS', 'MilkShake'),
    ('PN', 'Paneer'),
    ('GH', 'Ghee'),
    ('CZ', 'Cheese'),
    ('IC', 'Ice-Creams'),
   
    # เพิ่มตัวเลือกอื่นที่คุณต้องการ
)

# คลาส Product แทนตาราง (table) ผลิตภัณฑ์ในฐานข้อมูล
class Product(models.Model):
    title = models.CharField(max_length=100)  # ชื่อของผลิตภัณฑ์ ความยาวสูงสุด 100 ตัวอักษร
    selling_price = models.FloatField()  # ราคาขายของผลิตภัณฑ์ในรูปเป็น float
    discounted_price = models.FloatField()  # ราคาลดพิเศษของผลิตภัณฑ์ในรูปเป็น float
    description = models.TextField()  # คำอธิบายของผลิตภัณฑ์
    conposition = models.TextField(default='')  # องค์ประกอบของผลิตภัณฑ์ (default เป็นค่าว่าง)
    prodapp = models.TextField(default='')  # แอปพลิเคชันของผลิตภัณฑ์ (default เป็นค่าว่าง)
    category = models.CharField(choices=CATEGOTY_CHOICES, max_length=2)  # ประเภทของผลิตภัณฑ์ มีตัวเลือกจาก CATEGOTY_CHOICES ความยาวสูงสุด 2 ตัวอักษร
    product_image = models.ImageField(upload_to='product')  # รูปภาพผลิตภัณฑ์ อัปโหลดไปที่ directory 'product'
    
    def __str__(self):
        return self.title  # แสดงชื่อของผลิตภัณฑ์เมื่อทำการแสดงข้อมูลของออบเจ็กต์นี้
