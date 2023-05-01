from uuid import uuid4

import requests
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db.models import Q  # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from kale.settings import BOT_TOKEN, GROUP_CHAT_ID
from . import models
from .models import Header_Carusel, Category, Best_seller_products, Product, Form, GalleryPhotos1, \
    GalleryData1, About, CustomUser, Discount, Orders, ChatRoom, ChatMessage, BarabanDiscount


def telebot(mess):
    requests.get(
        url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={GROUP_CHAT_ID}&parse_mode=HTML&text={mess}")


class HeaderCaruselSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Header_Carusel
        fields = ['id', 'nomi_uz', 'nomi_ru', 'nomi_en',
                  'text_uz', 'text_ru', 'text_en',
                  'image']

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        else:
            return None


# class CatalogSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Catalog
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     catalog_name = CatalogSerializer(read_only=True)
#
#     class Meta:
#         model = Category
#         fields = ['id', 'name_uz', 'name_ru', 'name_en', 'catalog_name']


class BestSellerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Best_seller_products
        # fields = ['id', 'name', 'description', 'best_seller_product']
        fields = '__all__'

    def get_image(self, obj):
        if obj:
            return self.context['request'].build_absolute_uri(obj)
        else:
            return None


class Product_By_CategorySerializer(serializers.ModelSerializer):
    category_name_ru = serializers.CharField(source='category.name_ru', read_only=True)
    category_name_uz = serializers.CharField(source='category.name_uz', read_only=True)
    category_name_en = serializers.CharField(source='category.name_en', read_only=True)

    class Meta:
        model = Product
        fields = (
            'id', 'name_uz', 'name_en', 'name_ru', 'description_uz', 'description_ru', 'description_en', 'price',
            'image1', 'image2', 'image3', 'image4', 'image5',
            'korzinka', 'saralangan', 'code', 'count', 'category_name_uz', 'category_name_ru', 'category_name_en',
            'solishtirsh', 'best_seller_product')

    def get_image(self, obj):
        if obj.images.exists():
            return self.context['request'].build_absolute_uri(obj.images.first().image.url)
        else:
            return None


class Category_Serailzier(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name_uz', 'name_ru', 'name_en')


class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id', 'name', 'phone', 'address']

    def create(self, validated_data):
        # Create the object using the validated data
        my_object = Form.objects.create(**validated_data)

        # Send a message to the Telegram group
        message = f"New User: \n\n{my_object}"
        telebot(message)
        return my_object


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class GalleryPhotosSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryPhotos1
        fields = ['id', 'photo']


class GalleryDataSerializer(serializers.ModelSerializer):
    image = GalleryPhotosSerializer(read_only=True, many=True)

    class Meta:
        model = GalleryData1
        fields = ['id', 'title_uz', 'title_ru',
                  'title_en', 'text_uz',
                  'text_en', 'text_ru', 'image']


class CategorySerializer1(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_uz', 'name_ru', 'name_en']


class ProductSerializer1(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = ['id', 'name_uz', 'name_ru', 'name_en', 'description', 'price', 'image1', 'image2', 'image3', 'image4',
                  'image5',
                  'korzinka', 'code', 'count', 'saralangan', 'solishtirsh', 'best_seller_product', 'category',
                  'category_name']

    def get_category_name(self, obj):
        return obj.category.name_ru if obj.category else None


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


class InfoGrafikaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.InfoGrafika
        fields = '__all__'


class GalleryOnlyImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GalleryOnlyImages
        fields = '__all__'


class PartnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Partners
        fields = '__all__'


class GalleryNewsSerializer(serializers.ModelSerializer):
    time = serializers.DateTimeField(format='%d.%m.%Y %H:%M:%S')

    class Meta:
        model = models.Gallery_News
        fields = ['id', 'title_uz', 'title_ru', 'title_en',
                  'text_uz', 'text_ru', 'text_en',
                  'time', 'img']


class SocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SocialNetworks
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = '__all__'


class WorksByKaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.WorksByKale
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'

    def create(self, validated_data):
        # Create the object using the validated data
        my_object = Discount.objects.create(**validated_data)

        # Send a message to the Telegram group
        message = f"New User: \n\n{my_object}"
        telebot(message)
        return my_object


class OrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'

    def create(self, validated_data):
        # Create the object using the validated data
        my_object = Orders.objects.create(**validated_data)

        # Send a message to the Telegram group
        message = f"New User: \n\n{my_object}"
        telebot(message)
        return my_object


class ChatRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatRoom
        fields = '__all__'


class ChatMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChatMessage
        fields = '__all__'


class BarabanDiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = BarabanDiscount
        fields = '__all__'
