from django.contrib import admin
from .models import Bill
from .models import Product
# Register your models here.
admin.site.register(Bill)
admin.site.register(Product)

