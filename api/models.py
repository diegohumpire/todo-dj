from __future__ import unicode_literals

# Create your models here.
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __unicode__(self):
        return unicode(self.name)


class Invoice(models.Model):
    client = models.ForeignKey(Client)
    total = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.client)


class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(Invoice)
    product = models.ForeignKey(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __unicode__(self):
        return unicode('{0} - {1}').format(str(self.invoice), str(self.product))
