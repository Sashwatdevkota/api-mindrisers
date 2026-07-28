from django.contrib import admin
from .models import *


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


admin.site.register(Category, CategoryAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price", "category")
    search_fields = ("name",)
    list_filter = ("category",)


admin.site.register(Menu, MenuAdmin)


class TableAdmin(admin.ModelAdmin):
    list_display = ("id", "num", "is_available")
    list_filter = ("is_available",)


admin.site.register(Table, TableAdmin)


class OrderMenuInline(admin.TabularInline):
    model = OrderMenu
    autocomplete_fields = ("menu",)


class OrderAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "total_price", "status")
    inlines = [OrderMenuInline]


admin.site.register(Order, OrderAdmin)


# admin.site.register(OrderMenu)

# admin customization


# INTEGRATE NOTES INTO TO DO LIST
# ADMIN CUSTOMIZATION
