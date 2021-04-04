from django.contrib import admin
from django.utils.html import format_html

from .models import Product, ProductImage, Review


class ReviewInline(admin.TabularInline):
    model = Review


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductImageInline, ReviewInline, )
    list_display = ('title', 'price', 'in_stock', 'active', 'seller_name')
    list_filter = ('price', 'in_stock', 'date_updated',)
    list_editable = ('in_stock', 'active')
    search_fields = ('name',)
    autopopulate_fields = ('tags',)

    def seller_name(self, obj):
        return obj.seller.name


admin.site.register(Product, ProductAdmin)


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


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('review', 'author', 'product',)
    list_filter = ('author',)
    search_fields = ('product',)


admin.site.register(Review, ReviewAdmin)
