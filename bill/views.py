from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Bill
from .models import Product

# Create your views here.

def index(request):
    return render(request, 'input.html')

def bill_view(request):
    return render(request,'tax_invoice.html')

def to_gst(request):
    if request.method=="POST":
        to = request.POST.get("to")
        gstn  = request.POST.get("gst")
        invoice_no = request.POST.get("invoice_no")
        date = request.POST.get("date")
              
        bill = Bill.objects.create(to=to,byerGSTN=gstn,invoice_no=invoice_no,date=date)
        bill.save()
        
        return render(request,'addProd.html',{'bill':bill})


def prod_insert(request):
    if request.method=="POST":
        particulars = request.POST.get("particulars")
        qty = float(request.POST.get("qty"))
        rate = float(request.POST.get("rate"))
        bill = request.POST.get("bill")
        print("---------",bill,"----------")

        billObj = Bill.objects.get(to=bill)
        amount = qty*rate
        prod = Product.objects.create(particulars=particulars,qty=qty,rate=rate,amount=amount,bill=billObj)
        prod.save()

       
        prodObjArr = Product.objects.filter(bill__to=billObj.to)
        print("$$$$$ ",prodObjArr,"$$$$$$$")
        total = 0
        for prod in prodObjArr:
            total = total + prod.amount
        print("#####",total,"######")

        sgst = (total*9)/100
        cgst = (total*9)/100
       
        Gtotal = total+sgst+cgst

        b = Bill.objects.get(to=bill)
        b.total = total
        b.sgst = sgst
        b.cgst = cgst
        b.Gtotal = Gtotal
        b.save()
        
        return render(request,'addProd.html',{'bill':billObj})
    else:
        return render(request,'addProd.html')


def printDoc(request):
    bill = Bill.objects.get(id=int(request.GET.get("billID")))
    prods = Product.objects.filter(bill=bill)
    print("****",bill.to,"******")
    for i in prods:
        print(i)
    context = {
        "to":bill.to,
        "ByerGSTN":bill.byerGSTN,
        "invoice_no":bill.invoice_no,
        "date":bill.date,
        "total":bill.total,
        "sgst":bill.sgst,
        "cgst":bill.cgst,
        "Gtotal":bill.Gtotal,
        "prods":prods
    }
    print(context["cgst"])
    return render(request,'tax_invoice.html',context)
