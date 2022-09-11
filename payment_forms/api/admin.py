from django.contrib import admin
from django.contrib.admin.decorators import display

from .models import Item, Order


class ItemInline(admin.TabularInline):
    model = Order.items.through
    extra = 0


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "description", "price"]
    search_fields = ("name",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = (ItemInline,)
    list_display = ["id", "get_items"]
    exclude = ["items"]

    @display(description="items")
    def get_items(self, obj):
        return [item.name for item in obj.items.all()]
