from django.contrib import admin

from .models import Item


@admin.register(Item)
class ItemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price')
    search_fields = ('name',)
