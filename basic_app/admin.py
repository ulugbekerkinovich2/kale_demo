from django.contrib import admin

from basic_app import models
from basic_app.models import Best_seller_products


# admin.site.register(models.About)


class Best_SellerAdmin(admin.ModelAdmin):
    search_fields = ['name_en']
    # list_filter = ['name', 'best_seller_product']
    list_display = ['id']
    list_per_page = 500


class ProductsAdmin(admin.ModelAdmin):
    search_fields = ['code', 'name_ru']
    # list_filter = ['category']
    list_display = ['id', 'name_ru']
    # list_filter = ['category']
    list_per_page = 20


class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name_ru']
    # list_filter = ['name']
    # list_filter = ['name']
    list_display = ['id']
    list_per_page = 10


class Header_CaruselAdmin(admin.ModelAdmin):
    search_fields = ['id', 'nomi_ru']
    # list_filter = ['nomi']
    # list_filter = ['nomi']
    list_display = ['id']
    list_per_page = 10


class GalleryDataAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_display = ['id']
    list_per_page = 10


class GallerPhotosAdmin(admin.ModelAdmin):
    search_fields = ['id']
    list_per_page = 10


admin.site.register(models.CustomUser)
admin.site.register(models.Best_seller_products, Best_SellerAdmin)
admin.site.register(models.Orders)
admin.site.register(models.Discount)
admin.site.register(models.Header_Carusel, Header_CaruselAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product, ProductsAdmin)
admin.site.register(models.Form)
admin.site.register(models.GalleryData1, GalleryDataAdmin)
admin.site.register(models.GalleryPhotos1, GallerPhotosAdmin)
admin.site.register(models.InfoGrafika)
admin.site.register(models.GalleryOnlyImages)
admin.site.register(models.Partners)
admin.site.register(models.Gallery_News)
admin.site.register(models.SocialNetworks)
admin.site.register(models.Location)
admin.site.register(models.WorksByKale)
admin.site.register(models.About)
admin.site.register(models.BarabanDiscount)
