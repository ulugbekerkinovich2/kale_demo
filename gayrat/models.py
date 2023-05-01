from django.db import models

from gayrat.instances import get_shots_path


class Category(models.Model):
    name_uz = models.CharField(max_length=255, default='none', null=True, blank=True)
    name_ru = models.CharField(max_length=255, default='none', null=True, blank=True)
    name_en = models.CharField(max_length=255, default='none', null=True, blank=True)

    def __str__(self):
        return self.name_ru


class Product(models.Model):
    name_uz = models.CharField(max_length=255, default='name kiritilmagan')
    name_en = models.CharField(max_length=255, default='name kiritilmagan')
    name_ru = models.CharField(max_length=255, default='name kiritilmagan')
    description_uz = models.TextField(null=True, blank=True)
    description_en = models.TextField(null=True, blank=True)
    description_ru = models.TextField(null=True, blank=True)
    count = models.CharField(max_length=20, default='0')
    code = models.CharField(max_length=30, default='mahsulot kodi kiritilmagan', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    korzinka = models.BooleanField(default=False)
    saralangan = models.BooleanField(default=False)
    solishtirsh = models.BooleanField(default=False)
    best_seller_product = models.BooleanField(default=False)

    def __str__(self):
        return self.name_ru

    class Meta:
        verbose_name_plural = 'Product'


class ProductShots(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="shots")
    image = models.ImageField(upload_to=get_shots_path, null=True, blank=True)


