from django.contrib import admin

from .models import Seller


class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'is_active', 'owner',)


admin.site.register(Seller, SellerAdmin)
