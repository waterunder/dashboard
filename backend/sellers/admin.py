from django.contrib import admin
from products.models import Product

from .models import Seller


class ProductInline(admin.TabularInline):
    model = Product


class SellerAdmin(admin.ModelAdmin):
    inlines = (ProductInline, )
    list_display = ('name', 'email', 'city', 'zip_code', 'country', 'is_active', 'owner', 'created_at',)
    list_filter = ('is_active', 'created_at', 'country',)
    list_editable = ('is_active',)
    search_fields = ('name', 'email',)
    raw_id_fields = ('owner',)
    date_heirarchy = 'created_at'
    ordering = ('-is_active', 'created_at',)


admin.site.register(Seller, SellerAdmin)
