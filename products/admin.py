from django.contrib import admin

from .models import Product, Review


class ReviewInline(admin.TabularInline):
    model = Review


class ProductAdmin(admin.ModelAdmin):
    inlines = [ReviewInline, ]
    list_display = ('title', 'description', 'price',)


admin.site.register(Product, ProductAdmin)
