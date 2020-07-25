from django.contrib import admin

from .models import Product, ProductImage, ProductTag, Review


class ReviewInline(admin.TabularInline):
    model = Review


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImageInline, ReviewInline, )
    list_display = ('title', 'description', 'price',)


admin.site.register(Product, ProductAdmin)
