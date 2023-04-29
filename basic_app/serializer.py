from uuid import uuid4

import requests
from django.contrib.auth.hashers import make_password
from django.core.exceptions import ValidationError
from django.db.models import Q  # for queries
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from kale.settings import BOT_TOKEN, GROUP_CHAT_ID
from . import models
from .models import Header_Carusel, Catalog, Category, Best_seller_products, Product, Form, GalleryPhotos1, \
    GalleryData1, About, CustomUser
from .models import User


def telebot(mess):
    requests.get(
        url=f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage?chat_id={GROUP_CHAT_ID}&parse_mode=HTML&text={mess}")


class HeaderCaruselSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Header_Carusel
        fields = ['id', 'nomi', 'text', 'image']

    def get_image(self, obj):
        if obj.image:
            return self.context['request'].build_absolute_uri(obj.image.url)
        else:
            return None


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    catalog_name = CatalogSerializer(read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'name']


class BestSellerProductSerializer(serializers.ModelSerializer):
    # image = serializers.SerializerMethodField(source='image_urls')

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
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'price', 'image1', 'image2', 'image3', 'image4', 'image5',
                  'korzinka', 'saralangan', 'code', 'count', 'category_name',
                  'solishtirsh', 'best_seller_product')

    def get_image(self, obj):
        if obj.images.exists():
            return self.context['request'].build_absolute_uri(obj.images.first().image.url)
        else:
            return None


class Category_Serailzier(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


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
        fields = ['id', 'title', 'text', 'image']


class CategorySerializer1(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class ProductSerializer1(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = ['id', 'name', 'description', 'price', 'image1', 'image2', 'image3', 'image4', 'image5',
                  'korzinka', 'code', 'count', 'saralangan', 'solishtirsh', 'best_seller_product', 'category',
                  'category_name']

    def get_category_name(self, obj):
        return obj.category.name if obj.category else None


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
        fields = ['id', 'title', 'text', 'time', 'img']


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


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategoryProduct
        fields = ('id', 'name')


class SubCategoryProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = models.SubCategory
        fields = ('id', 'sub_category', 'category_name')


class UserSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(max_length=8)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)

    class Meta:
        model = User
        fields = (
            'username',
            'phone_number',
            'password'
        )


class UserLoginSerializer(serializers.ModelSerializer):
    # to accept either username or email
    user_id = serializers.CharField()
    password = serializers.CharField()
    token = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        # user,email,password validator
        user_id = data.get("user_id", None)
        password = data.get("password", None)
        if not user_id and not password:
            raise ValidationError("Details not entered.")
        user = None
        # if the email has been passed
        if len(user_id) >= 7:
            user = User.objects.filter(
                Q(phone_number=user_id) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(phone_number=user_id)
        else:
            user = User.objects.filter(
                Q(username=user_id) &
                Q(password=password)
            ).distinct()
            if not user.exists():
                raise ValidationError("User credentials are not correct.")
            user = User.objects.get(username=user_id)
        if user.ifLogged:
            raise ValidationError("User already logged in.")
        user.ifLogged = True
        data['token'] = uuid4()
        user.token = data['token']
        user.save()
        return data

    class Meta:
        model = User
        fields = (
            'user_id',
            'password',
            'token',
        )

        read_only_fields = (
            'token',
        )


class UserLogoutSerializer(serializers.ModelSerializer):
    token = serializers.CharField()
    status = serializers.CharField(required=False, read_only=True)

    def validate(self, data):
        token = data.get("token", None)
        print(token)
        user = None
        try:
            user = User.objects.get(token=token)
            if not user.ifLogged:
                raise ValidationError("User is not logged in.")
        except Exception as e:
            raise ValidationError(str(e))
        user.ifLogged = False
        user.token = ""
        user.save()
        data['status'] = "User is logged out."
        return data

    class Meta:
        model = User
        fields = (
            'token',
            'status',
        )


class UserDataSerializer1(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'password', 'user_phone']
        # exclude = ['best_seller_product']

