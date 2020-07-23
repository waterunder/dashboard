from django.contrib import admin

from products.models import Product

from .models import Seller


class ProductInline(admin.TabularInline):
    model = Product


class SellerAdmin(admin.ModelAdmin):
    inlines = (ProductInline, )
    list_display = ('name', 'email', 'country', 'is_active', 'owner',)


admin.site.register(Seller, SellerAdmin)
