from django.db import models
from django.db.models.deletion import CASCADE
import datetime
# Create your models here.


class Bill(models.Model):
    to = models.CharField(max_length=50,null=True)
    byerGSTN = models.CharField(max_length=50,null=True)
    invoice_no = models.BigIntegerField(null=True)
    date = models.DateTimeField(auto_now_add=True,null=True)
    total = models.FloatField(null=True)
    sgst = models.FloatField(null=True)
    cgst = models.FloatField(null=True)
    Gtotal = models.FloatField(null=True)

    def __str__(self):
        return "%s" %(self.to)

class Product(models.Model):
    particulars = models.CharField(max_length=50,null=True)
    qty = models.BigIntegerField(null=True)
    rate = models.FloatField(null=True)
    amount = models.FloatField(null=True)
    bill = models.ForeignKey(Bill, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.particulars

