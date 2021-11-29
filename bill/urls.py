from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="bill"),
    path('to_gst',views.to_gst,name="to_gst"),
    path('prod_insert',views.prod_insert,name="prod_insert"),
    path('printDoc',views.printDoc,name="printDoc"),
    path('bill_view', views.bill_view,name="bill_view"),
]
