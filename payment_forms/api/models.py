from django.db import models
from djmoney.models.fields import MoneyField


class Item(models.Model):
    name = models.CharField('Name', max_length=256)
    description = models.CharField('Description', max_length=256, null=True, blank=True)
    price = MoneyField(max_digits=14, decimal_places=4, default_currency='USD')

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.name


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name="order_items")

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f'Order number: {self.id}'
