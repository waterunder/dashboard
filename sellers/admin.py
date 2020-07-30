from django.contrib import admin

from products.models import Product

from .models import Seller


class ProductInline(admin.TabularInline):
    model = Product


class SellerAdmin(admin.ModelAdmin):
    inlines = (ProductInline, )
    list_display = ('name', 'email', 'country', 'is_active', 'owner',)
    list_filter = ('name', 'country',)
    list_editable = ('is_active',)


admin.site.register(Seller, SellerAdmin)
