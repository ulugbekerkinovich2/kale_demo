from django.contrib.auth.hashers import make_password
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.

#
class About(models.Model):
    image = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=255, null=True, blank=True)
    text = models.TextField(blank=True, null=True, default='matn kiritilmagan')

    def __str__(self):
        return self.title

    def url(self):
        if self.image:
            return self.image.url
        else:
            return ''

    class Meta:
        verbose_name_plural = 'About'


class CustomUserManager(BaseUserManager):
    def create_user(self, username, **extra_fields):

        if not username:
            raise ValueError(_('The name must be set'))

        user = self.model(username=username, **extra_fields)
        user.set_password(extra_fields['password'])
        user.save()
        return user

    def create_superuser(self, username, **extra_fields):

        extra_fields.setdefault('is_staff', True)

        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_active') is not True:
            raise ValueError(_('Superuser must have is_active=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(username=username, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(_('Name'), max_length=50, unique=True)
    user_phone = models.CharField(_('Phone Number'), max_length=20,
                                  unique=True, null=True, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateField(default=timezone.now)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    #     def save(self, *args, **kwargs):
    #         # Hash the password before saving
    #         self.password = make_password(self.password)
    #         super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.username}'


class Catalog(models.Model):
    name = models.TextField(blank=False, verbose_name='catalog_name')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'catalog'
        verbose_name_plural = 'catalog'


class Header_Carusel(models.Model):
    nomi = models.CharField(max_length=200, default='none', null=True, blank=True)
    text = models.TextField(default='none', null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f'ID: {self.id}    {self.nomi}'

    def image_url(self):
        urls = []
        for img in self.image.all():
            urls.append(img.url())
        return urls

    class Meta:
        verbose_name_plural = 'header_carusel'


class Best_seller_products(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    code = models.CharField(max_length=300, null=True, blank=True)
    image_1 = models.ImageField(upload_to='best_seller_images/', null=True, blank=True)
    image_2 = models.ImageField(upload_to='best_seller_images/', null=True, blank=True)
    image_3 = models.ImageField(upload_to='best_seller_images/', null=True, blank=True)
    image_4 = models.ImageField(upload_to='best_seller_images/', null=True, blank=True)
    image_5 = models.ImageField(upload_to='best_seller_images/', null=True, blank=True)
    korzinka = models.BooleanField(default=False)
    saralangan = models.BooleanField(default=False)
    solishtirsh = models.BooleanField(default=False)
    best_seller_product = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def image_urls(self, request):
        urls = []
        for field_name in ['image_1', 'image_2', 'image_3', 'image_4', 'image_5']:
            image = getattr(self, field_name, None)
            if image:
                url = request.build_absolute_uri(image.url)
                urls.append(url)
        return urls

    class Meta:
        verbose_name_plural = 'Best Seller Products'


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=255, null=False)
    phone_number = models.CharField(max_length=255, null=False)
    password = models.CharField(max_length=50)
    ifLogged = models.BooleanField(default=False)
    token = models.CharField(max_length=500, null=True, default="")

    def __str__(self):
        return self.phone_number


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    count = models.CharField(max_length=20, default='0')
    code = models.CharField(max_length=30, default='mahsulot kodi kiritilmagan', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='images/', null=True, blank=True)
    image3 = models.ImageField(upload_to='images/', null=True, blank=True)
    image4 = models.ImageField(upload_to='images/', null=True, blank=True)
    image5 = models.ImageField(upload_to='images/', null=True, blank=True)
    korzinka = models.BooleanField(default=False)
    saralangan = models.BooleanField(default=False)
    solishtirsh = models.BooleanField(default=False)
    best_seller_product = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Form(models.Model):
    name = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Ismi: {self.name}\nTelefon raqami: {self.phone}\nManzil: {self.address}'

    class Meta:
        verbose_name_plural = 'Form'


class GalleryPhotos1(models.Model):
    photo = models.ImageField(upload_to='galery_images/', null=True, blank=True)

    def __str__(self):
        return str(self.photo)

    class Meta:
        verbose_name_plural = 'Gallery_photos'


class GalleryData1(models.Model):
    title = models.TextField(default='matn kiritilmagan', null=True, blank=True)
    text = models.TextField(default='matn kiritilmagan', null=True, blank=True)
    image = models.ManyToManyField(GalleryPhotos1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Gallery_data'


class InfoGrafika(models.Model):
    nominal_product = models.CharField(max_length=30, default='40')
    partners = models.CharField(max_length=30, default='10')
    nominal_products = models.CharField(max_length=30, default='40')
    nominal_products_last = models.CharField(max_length=30, default='40')

    def __str__(self):
        return self.nominal_product

    class Meta:
        verbose_name_plural = 'infografika'


class GalleryOnlyImages(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name_plural = 'Gallery_Only_Images'


class Partners(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.image.name

    class Meta:
        verbose_name_plural = 'Partners'


class Gallery_News(models.Model):
    title = models.CharField(max_length=512, default='matn kiritilmagan')
    text = models.TextField(default='matn kiritilmagan')
    img = models.ImageField(upload_to='images/')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.time.strftime('%d.%m.%Y') if self.time else 'no time set'}"

    class Meta:
        verbose_name = 'Gallery News'
        verbose_name_plural = 'Gallery News'


class SocialNetworks(models.Model):
    instagram_link = models.URLField(max_length=512, default='link kiritilmagan', null=True, blank=True)
    facebook_link = models.URLField(max_length=512, default='link kiritilmagan', null=True, blank=True)
    telegram_link = models.URLField(max_length=512, default='link kiritilmagan', null=True, blank=True)
    youtube_link = models.URLField(max_length=512, default='link kiritilmagan', null=True, blank=True)
    whatsapp_link = models.URLField(max_length=512, default='link kiritilmagan', null=True, blank=True)
    linkedin_link = models.URLField(max_length=512, default='link kiritilmagan', null=True, blank=True)
    twitter_link = models.URLField(max_length=512, default='link kiritilmagan', null=True, blank=True)
    tiktok_link = models.URLField(max_length=512, default='link kiritilmagan', null=True, blank=True)
    pinterest_link = models.URLField(max_length=512, default='link kiritilmagan', null=True, blank=True)

    def __str__(self):
        return self.instagram_link

    class Meta:
        verbose_name_plural = 'Social_Networks'


class Location(models.Model):
    title = models.CharField(max_length=512, default='matn kiritilmagan', null=True, blank=True)
    text = models.TextField(default='matn kiritilmagan', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Location'


class WorksByKale(models.Model):
    title = models.CharField(max_length=512, default='matn kiritilmagan', null=True, blank=True)
    text = models.TextField(default='matn kiritilmagan', null=True, blank=True)
    image1 = models.ImageField(upload_to='images/', null=True, blank=True)
    image2 = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Works_By_Kale'


class CategoryProduct(models.Model):
    name = models.CharField(max_length=512, default='matn kiritilmagan', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Category_Product'


class SubCategory(models.Model):
    category = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE)
    sub_category = models.CharField(max_length=512, default='matn kiritilmagan', null=True, blank=True)

    def __str__(self):
        return self.sub_category

    class Meta:
        verbose_name_plural = 'Sub_Category'


class Discount(models.Model):
    name = models.CharField(max_length=512, default='matn kiritilmagan', null=True, blank=True)
    phone_number = models.CharField(max_length=512, default='matn kiritilmagan', null=True, blank=True)
    location = models.CharField(max_length=512, default='matn kiritilmagan', null=True, blank=True)
    discount_name = models.CharField(max_length=512, default='matn kiritilmagan', null=True, blank=True)
    total_cost = models.IntegerField(default=0)

    def __str__(self):
        return f"Ismi: {self.name}\n" \
               f"Telefon raqami: {self.phone_number}\n" \
               f"Manzili: {self.location}\n" \
               f"Chegirma nomi: {self.discount_name}\n" \
               f"Umumiy narxi: {self.total_cost}"

    class Meta:
        verbose_name_plural = 'Discount'
