from django.contrib import admin
from django.utils.html import format_html

from .models import Product, ProductImage, ProductTag, Review


class ReviewInline(admin.TabularInline):
    model = Review


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImageInline, ReviewInline, )
    list_display = ('title', 'price', 'in_stock', 'seller')
    list_filter = ('price', 'in_stock', 'date_updated',)
    list_editable = ('in_stock',)
    search_fields = ('name',)
    autocomplete_fields = ('tags',)


class ProductTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'active')
    list_editable = ('active',)
    list_filter = ('active',)
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductTag, ProductTagAdmin)


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('thumbnail_tag', 'product_name')
    readonly_fields = ('thumbnail',)
    search_fields = ('product__name',)

    def thumbnail_tag(self, obj):
        if obj.thumbnail:
            return format_html(
                '<img src="%s"/>' % obj.thumbnail.url
            )
        return "-"
    thumbnail_tag.short_description = 'Thumbnail'

    def product_name(self, obj):
        return obj.product.name


admin.site.register(ProductImage, ProductImageAdmin)
