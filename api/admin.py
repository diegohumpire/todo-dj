from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import ugettext_lazy


# Register your models here.
from .models import Client, Product, Invoice, InvoiceDetail

admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Invoice)
admin.site.register(InvoiceDetail)
