from django.contrib import admin

from gayrat.models import Category, ProductShots, Product


class ProductShotsInlineAdmin(admin.TabularInline):
    model = ProductShots
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductShotsInlineAdmin]


@admin.register(ProductShots)
class ProductAdmin(admin.ModelAdmin):
    ...


@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    ...
