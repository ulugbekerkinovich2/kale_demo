import requests
from django.core.cache import cache
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import JsonResponse
from django.shortcuts import redirect
from rest_framework import filters, viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from kale import settings
from kale.settings import username, password
from . import models, serializer
from .models import Best_seller_products, Category, Product, ChatRoom, ChatMessage
from .models import Header_Carusel
from .serializer import HeaderCaruselSerializer, BestSellerProductSerializer, InfoGrafikaSerializer, ChatRoomSerializer, \
    ChatMessageSerializer

obj = []

url = "http://94.158.52.249/Base/hs/info/stocks/"


# class IntegrateData(generics.ListAPIView):
#     def get(self, request):
#         # url = "http://94.158.52.249/Base/hs/info/stocks/"
#         response = requests.get(url, auth=(username, password))
#         if response.content:
#             json_data = response.json()

#             data = json_data['Товары']
#             data_category = set()

#             for item in data:
#                 nomlanishi = item['Наименование']
#                 kodi = item['Код']
#                 birlik = item['ЕдиницаИзмерения']
#                 markasi = item['ТорговаяМарка']
#                 razmeri = item['Размеры']
#                 text = item['Описание']
#                 ishlab_chiqaruvchi = item['Производитель']
#                 kategoriya = item['Категория']
#                 qolgan_mahsulot = item['Остаток']
#                 narxi = item['Цена']
#                 obj.append(kodi)
#                 if kategoriya != '':
#                     data_category.add(kategoriya)

#             data_json = {}
#             for category in data_category:
#                 data_json[category] = []

#             for item in data:
#                 nomlanishi = item['Наименование']
#                 kodi = item['Код']
#                 birlik = item['ЕдиницаИзмерения']
#                 markasi = item['ТорговаяМарка']
#                 razmeri = item['Размеры']
#                 text = item['Описание']
#                 ishlab_chiqaruvchi = item['Производитель']
#                 kategoriya = item['Категория']
#                 qolgan_mahsulot = item['Остаток']
#                 narxi = item['Цена']
#                 json_obj = {
#                     "nomlanishi": nomlanishi,
#                     "kodi": kodi,
#                     'birlik': birlik,
#                     'markasi': markasi,
#                     'razmeri': razmeri,
#                     'text': text,
#                     'ishlab_chiqaruvchi': ishlab_chiqaruvchi,
#                     'qolgan_mahsulot': qolgan_mahsulot,
#                     'narxi': narxi,
#                     # 'image': data_img,
#                 }
#                 # if not Header_Carusel.objects.filter(title=nomlanishi, description=text).exists():
#                 #     header = Header_Carusel(title=nomlanishi, description=text)
#                 #     header.save()

#                 if kategoriya in data_category:
#                     data_json[kategoriya].append(json_obj)

#             return Response(data_json)

#     pagination_class = PageNumberPagination


class HeaderCarouselList(APIView):
    def get(self, request, id=None, count=None):
        cache_key = 'header_carousel_data'

        # Try to retrieve data from cache
        headers = cache.get(cache_key)
        if headers is None:
            response = requests.get(url, auth=(username, password))
            json_data = response.json()
            data = json_data.get('Товары', [])

            for item in data:
                nomi = item.get('Наименование')
                text = item.get('Описание')
                if nomi and text and not Header_Carusel.objects.filter(nomi=nomi, text=text).exists():
                    header = Header_Carusel(nomi=nomi, text=text)
                    header.save()

            # Get data from the database and save it to cache
            headers = Header_Carusel.objects.all().order_by('-id')
            cache.set(cache_key, headers, timeout=settings.CACHE_TIME)
        else:
            # Retrieve data from cache
            headers = cache.get(cache_key)

        if id:
            # Filter the headers by id
            headers = headers.filter(id=id)

        if count:
            # Slice the headers to return the desired number of items
            headers = headers[:count]

        serializer = HeaderCaruselSerializer(headers, many=True, context={'request': request})
        return Response(serializer.data)


class ListHeaderCarousel(generics.ListAPIView):
    queryset = Header_Carusel.objects.all().order_by('-id')
    serializer_class = HeaderCaruselSerializer


# class BestSellerProductsList1(APIView):
#     def get(self, request, id=None, count=None):
#         cache_key = 'best_seller_data1'
#
#         # Try to retrieve data from cache
#         headers = cache.get(cache_key)
#
#         if headers is None:
#             response = requests.get(url, auth=(username, password))
#             json_data = response.json()
#             data = json_data['Товары']
#
#             # Save data to the model if it doesn't exist
#             for item in data:
#                 nomi = item['Наименование']
#                 text = item['Описание']
#                 kodi = item['Код']
#                 if not Best_seller_products.objects.filter(name=nomi, description=text, code=kodi).exists():
#                     header = Best_seller_products(name=nomi, description=text, code=kodi)
#                     header.save()
#             headers = Best_seller_products.objects.all().order_by('-id')
#             # latest_products = Best_seller_products.objects.filter(name=OuterRef('name')).order_by('-id')
#
#             # Best_seller_products.objects.annotate(
#             #     latest_id=Subquery(latest_products.values('id')[:1])).exclude(id=F('latest_id')).delete()
#             cache.set(cache_key, headers, timeout=settings.CACHE_TIME)
#         if id:
#             for header in headers:
#                 if header.id == id:
#                     headers = [header]
#                     break
#
#
#         # Get data by count if count parameter is provided
#         elif count:
#             headers = headers[:count]
#
#         serializer = BestSellerProductSerializer(headers, many=True, context={'request': request})
#         return Response(serializer.data)


# @api_view(['GET'])
# def products_by_category3_(request):
#     count = request.GET.get('count')
#     # latest_products = Product.objects.filter(name=OuterRef('name')).order_by('-id')
#     #
#     # # Delete all products that are not the latest one with a given name
#     # Product.objects.annotate(latest_id=Subquery(latest_products.values('id')[:1])).exclude(id=F('latest_id')).delete()
#     cache_key_all = "products_by_category:all"
#     data_all = cache.get(cache_key_all)
#
#     # If data is not found in cache, fetch from API
#     if data_all is None:
#         response = requests.get(url, auth=(username, password))
#         if response.status_code != 200:
#             return Response({'error': 'Failed to fetch data from API'})
#
#         # Process the JSON data and create Category and Product objects
#         json_data = response.json()
#         products_data = json_data.get('Товары', [])
#         categories = {}
#         for product_data in products_data:
#             category_name = product_data.get('Категория', '').strip()
#             if category_name:
#                 categories[category_name] = categories.get(category_name, []) + [product_data]
#         products = []
#         for category_name, products_data in categories.items():
#             category, created = Category.objects.get_or_create(name=category_name)
#             for product_data in products_data:
#                 product = Product(name=product_data['Наименование'],
#                                   description=product_data['Описание'],
#                                   price=product_data['Цена'],
#                                   category=category,
#                                   image1=product_data.get('image1', 'None'),
#                                   image2=product_data.get('image2', 'None'),
#                                   image3=product_data.get('image3', 'None'),
#                                   image4=product_data.get('image4', 'None'),
#                                   image5=product_data.get('image5', 'None'),
#                                   korzinka=product_data.get('korzinka', False),
#                                   saralangan=product_data.get('saralangan', False),
#                                   solishtirsh=product_data.get('solishtirsh', False),
#                                   best_seller_product=product_data.get('best_seller_product', False))
#                 products.append(product)
#         Product.objects.bulk_create(products)
#         products = Product.objects.select_related('category').all()
#         data_all = {}
#         for product in products:
#             category_name = product.category.name
#             product_data = {
#                 'id': product.id,
#                 'name': product.name,
#                 'description': product.description,
#                 'price': product.price,
#                 'image1': product.image1.url if product.image1 else 'None',
#                 'image2': product.image2.url if product.image2 else 'None',
#                 'image3': product.image3.url if product.image3 else 'None',
#                 'image4': product.image4.url if product.image4 else 'None',
#                 'image5': product.image5.url if product.image5 else 'None',
#                 'korzinka': product.korzinka,
#                 'saralangan': product.saralangan,
#                 'solishtirsh': product.solishtirsh,
#                 'best_seller_product': product.best_seller_product
#             }
#             data_all[category_name] = data_all.get(category_name, []) + [product_data]
#
#         # Cache the data for future requests
#         cache.set(cache_key_all, data_all, timeout=settings.CACHE_TIME)
#
#     # Check if cache for filtered data exists and return if found
#     if count:
#         cache_key = f"products_by_category:{count}"
#         data = cache.get(cache_key)
#         if data is not None:
#             return Response(data)
#
#         # Filter data by count if cache not found
#         data = {}
#         for category_name, products_data in data_all.items():
#             data[category_name] = data_all[category_name][:int(count)]
#             # Cache the filtered data
#             cache.set(cache_key, data, timeout=settings.CACHE_TIME)
#
#         return Response(data)
#
#     return Response(data_all)


class ListCategory(generics.ListAPIView):
    queryset = models.Category.objects.all()
    serializer_class = serializer.CategorySerializer1


class ListWorksByKale(generics.ListAPIView):
    queryset = models.WorksByKale.objects.all()
    serializer_class = serializer.WorksByKaleSerializer


class ProductSearch(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']


class ListForm(generics.ListCreateAPIView):
    queryset = models.Form.objects.all()
    serializer_class = serializer.FormSerializer


class ListGalleryData1(generics.ListAPIView):
    queryset = models.GalleryData1.objects.all()
    serializer_class = serializer.GalleryDataSerializer


class DetailGalleryData1(generics.RetrieveAPIView):
    queryset = models.GalleryData1.objects.all()
    serializer_class = serializer.GalleryDataSerializer


class ListGalleryPhotos1(generics.ListAPIView):
    queryset = models.GalleryPhotos1.objects.all()
    serializer_class = serializer.GalleryPhotosSerializer


class DetailGalleryPhotos1(generics.RetrieveAPIView):
    queryset = models.GalleryPhotos1.objects.all()
    serializer_class = serializer.GalleryPhotosSerializer


class ListAbout(generics.ListAPIView):
    queryset = models.About.objects.all().order_by('id')
    serializer_class = serializer.AboutSerializer
    pagination_class = None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer_ = self.get_serializer(queryset, many=True)
        return Response(serializer_.data)


@api_view(['GET'])
def products_by_category3__(request):
    count = request.GET.get('count')
    cache_key_all = "products_by_category:all"
    data_all = cache.get(cache_key_all)

    # If data is not found in cache, fetch from API
    if not data_all:
        response = requests.get(url, auth=(username, password))
        if response.status_code != 200:
            return Response({'error': 'Failed to fetch data from API'})

        # Process the JSON data and create Cate     gory and Product objects
        json_data = response.json()
        products_data = json_data.get('Товары', [])
        categories = {}
        products = []
        for product_data in products_data:
            category_name = product_data.get('Категория', '').strip()
            if category_name:
                category_queryset = Category.objects.filter(name=category_name)
                if category_queryset.exists():
                    category = category_queryset.first()
                else:
                    category = Category.objects.create(name=category_name)
                product_name = product_data.get('Наименование')
                try:
                    product = Product.objects.get(name=product_name, category=category)
                except ObjectDoesNotExist:
                    product = Product(name=product_name,
                                      description=product_data['Описание'],
                                      price=product_data['Цена'],
                                      category=category,
                                      code=product_data['Код'],
                                      count=product_data['Остаток'],
                                      image1=product_data.get('image1', 'None'),
                                      image2=product_data.get('image2', 'None'),
                                      image3=product_data.get('image3', 'None'),
                                      image4=product_data.get('image4', 'None'),
                                      image5=product_data.get('image5', 'None'),
                                      korzinka=product_data.get('korzinka', False),
                                      saralangan=product_data.get('saralangan', False),
                                      solishtirsh=product_data.get('solishtirsh', False),
                                      best_seller_product=product_data.get('best_seller_product', False))
                    products.append(product)
                except MultipleObjectsReturned:
                    # Handle multiple products with the same name and category here
                    pass
        Product.objects.bulk_create(products)
        products = Product.objects.select_related('category').all().order_by('-id')
        data_all = {}
        for product in products:
            category_name = product.category.name
            product_data = {
                'id': product.id,
                'name': product.name,
                'description': product.description,
                'price': product.price,
                'count': product.count,
                'code': product.code,
                'image1': product.image1.url if product.image1 else 'None',
                'image2': product.image2.url if product.image2 else 'None',
                'image3': product.image3.url if product.image3 else 'None',
                'image4': product.image4.url if product.image4 else 'None',
                'image5': product.image5.url if product.image5 else 'None',
                'korzinka': product.korzinka,
                'saralangan': product.saralangan,
                'solishtirsh': product.solishtirsh,
                'best_seller_product': product.best_seller_product
            }
            data_all[category_name] = data_all.get(category_name, []) + [product_data]

        # Cache the data for future requests
        cache.set(cache_key_all, data_all, timeout=settings.CACHE_TIME)

    # Check if cache for filtered data exists and return if found
    if count:
        cache_key = f"products_by_category:{count}"
        data = cache.get(cache_key)
        if data is not None:
            return Response(data)
        data = {}
        for category_name, products_data in data_all.items():
            data[category_name] = data_all[category_name][:int(count)]
            # Cache the filtered data
            cache.set(cache_key, data, timeout=settings.CACHE_TIME)

        return Response(data)

    return Response(data_all)


class ListProductsByCategory(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.Product_By_CategorySerializer

    def list(self, request, *args, **kwargs):
        cache_key = "products_by_category:all"
        data_all = cache.get(cache_key)
        response = requests.get(url, auth=(username, password))
        if response.status_code != 200:
            return Response({'error': 'Failed to fetch data from API'})
        if not data_all:
            json_data = response.json()
            products_data = json_data.get('Товары', [])
            products = []
            for product_data in products_data:
                category_name = product_data.get('Категория', '').strip()
                if category_name:
                    name_category = Category.objects.filter(name=category_name)
                    if name_category.exists():
                        category = name_category.first()
                    else:
                        category = Category.objects.create(name=category_name)
                    product_name = product_data.get('Наименование')
                    try:
                        category = Product.objects.get(name=product_name, category=category)
                    except ObjectDoesNotExist:
                        product = Product(name=product_name,
                                          description=product_data['Описание'],
                                          price=product_data['Цена'],
                                          category=category,
                                          code=product_data['Код'],
                                          count=product_data['Остаток'],
                                          image1=product_data.get('image1', 'None'),
                                          image2=product_data.get('image2', 'None'),
                                          image3=product_data.get('image3', 'None'),
                                          image4=product_data.get('image4', 'None'),
                                          image5=product_data.get('image5', 'None'),
                                          korzinka=product_data.get('korzinka', False),
                                          saralangan=product_data.get('saralangan', False),
                                          solishtirsh=product_data.get('solishtirsh', False),
                                          best_seller_product=product_data.get('best_seller_product', False))
                        products.append(product)
                    except MultipleObjectsReturned:
                        pass
            Product.objects.bulk_create(products)
            queryset = Product.objects.all()
            cache.set(cache_key, queryset, timeout=settings.CACHE_TIME)
            queryset = Product.objects.all()
            serializer_ = self.get_serializer(queryset, many=True)
            return Response(serializer_.data)
        # serializer_ = self.get_serializer(data_all, many=True)
        return Response(data_all)


class DetailProductByCategory(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer


class ListInfoGrafika(generics.ListAPIView):
    queryset = models.InfoGrafika.objects.all().order_by('-id')
    serializer_class = InfoGrafikaSerializer


class ListGalleryOnlyImages(generics.ListAPIView):
    queryset = models.GalleryOnlyImages.objects.all()
    serializer_class = serializer.GalleryOnlyImagesSerializer


class ListPartners(generics.ListAPIView):
    queryset = models.Partners.objects.all()
    serializer_class = serializer.PartnersSerializer


class ListGalleryNews(generics.ListAPIView):
    queryset = models.Gallery_News.objects.all()
    serializer_class = serializer.GalleryNewsSerializer


class DetailGalleryNews(generics.RetrieveAPIView):
    queryset = models.Gallery_News.objects.all()
    serializer_class = serializer.GalleryNewsSerializer


class ListProductsByCategory1(generics.ListAPIView):
    queryset = models.Product.objects.all().order_by('-id')
    serializer_class = serializer.Product_By_CategorySerializer

    def list(self, request, *args, **kwargs):
        cache_key = "products_by_category:all"
        data_all = cache.get(cache_key)
        if data_all is not None:
            # Sort the data by -id and return it
            sorted_data = sorted(data_all, key=lambda x: x['id'], reverse=True)
            return Response(sorted_data)

        # Data is not available in cache, fetch it from API or database
        response = requests.get(url, auth=(username, password), params={'sort_by': '-id'})
        if response.status_code != 200:
            return Response({'error': 'Failed to fetch data from API'})

        # Process the data and create Product objects
        json_data = response.json()
        products_data = json_data.get('Товары', [])
        products = []
        for product_data in products_data:
            category_name = product_data.get('Категория', '').strip()
            if category_name:
                name_category = Category.objects.filter(name=category_name)
                if name_category.exists():
                    category = name_category.first()
                else:
                    category = Category.objects.create(name=category_name)
                product_name = product_data.get('Наименование')
                try:
                    category = Product.objects.get(name=product_name, category=category)
                except ObjectDoesNotExist:
                    product = Product(name=product_name,
                                      description=product_data['Описание'],
                                      price=product_data['Цена'],
                                      category=category,
                                      code=product_data['Код'],
                                      count=product_data['Остаток'],
                                      image1=product_data.get('image1', 'None'),
                                      image2=product_data.get('image2', 'None'),
                                      image3=product_data.get('image3', 'None'),
                                      image4=product_data.get('image4', 'None'),
                                      image5=product_data.get('image5', 'None'),
                                      korzinka=product_data.get('korzinka', False),
                                      saralangan=product_data.get('saralangan', False),
                                      solishtirsh=product_data.get('solishtirsh', False),
                                      best_seller_product=product_data.get('best_seller_product', False))
                    products.append(product)
                except MultipleObjectsReturned:
                    pass

        # Bulk create the Product objects
        products_sorted = sorted(products, key=lambda p: p.id, reverse=True)
        Product.objects.bulk_create(products_sorted)

        # Retrieve the Product queryset from the database and serialize the data
        queryset = Product.objects.all().order_by('-id')
        serializer_ = self.get_serializer(queryset, many=True)

        # Store the serialized data in cache and return it
        cache.set(cache_key, serializer_.data, timeout=settings.CACHE_TIME)
        return Response(serializer_.data)


class ListProductsByCategory122(generics.ListAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.Product_By_CategorySerializer

    def list(self, request, *args, **kwargs):
        cache_key = "products_by_category:all"
        data_all = cache.get(cache_key)

        if data_all is not None:
            # Data is available in cache, return it
            return Response(data_all)

        # Data is not available in cache, fetch it from API or database
        response = requests.get(url, auth=(username, password))
        if response.status_code != 200:
            return Response({'error': 'Failed to fetch data from API'})

        # Process the data and create Product objects
        json_data = response.json()
        products_data = json_data.get('Товары', [])
        updated_products = []
        last_products = []
        for product_data in products_data:
            category_name = product_data.get('Категория', '').strip()
            if category_name:
                name_category = Category.objects.filter(name=category_name)
                if name_category.exists():
                    category = name_category.first()
                else:
                    category = Category.objects.create(name=category_name)
                product_name = product_data.get('Наименование')
                try:
                    product = Product.objects.get(name=product_name, category=category)
                    product.description = product_data['Описание']
                    product.price = product_data['Цена']
                    product.code = product_data['Код']
                    product.count = product_data['Остаток']
                    product.image1 = product_data.get('image1', 'None')
                    product.image2 = product_data.get('image2', 'None')
                    product.image3 = product_data.get('image3', 'None')
                    product.image4 = product_data.get('image4', 'None')
                    product.image5 = product_data.get('image5', 'None')
                    product.korzinka = product_data.get('korzinka', False)
                    product.saralangan = product_data.get('saralangan', False)
                    product.solishtirsh = product_data.get('solishtirsh', False)
                    product.best_seller_product = product_data.get('best_seller_product', False)
                    product.save()
                    updated_products.append(product)
                except ObjectDoesNotExist:
                    product = Product(name=product_name,
                                      description=product_data['Описание'],
                                      price=product_data['Цена'],
                                      category=category,
                                      code=product_data['Код'],
                                      count=product_data['Остаток'],
                                      image1=product_data.get('image1', 'None'),
                                      image2=product_data.get('image2', 'None'),
                                      image3=product_data.get('image3', 'None'),
                                      image4=product_data.get('image4', 'None'),
                                      image5=product_data.get('image5', 'None'),
                                      korzinka=product_data.get('korzinka', False),
                                      saralangan=product_data.get('saralangan', False),
                                      solishtirsh=product_data.get('solishtirsh', False),
                                      best_seller_product=product_data.get('best_seller_product', False))
                    product.save()
                    last_products.append(product)
                except MultipleObjectsReturned:
                    pass

                    # Serialize the updated and un-updated products and return them in separate arrays
        updated_serializer = self.get_serializer(updated_products, many=True)
        unupdated_serializer = self.get_serializer(last_products, many=True)
        data = {
            'updated_products': updated_serializer.data,
            'unupdated_products': unupdated_serializer.data}

        # Save the data to cache
        cache.set(cache_key, data, timeout=settings.CACHE_TIME)

        # Return the data
        return Response(data)


class DetailProductsByCategory1(generics.RetrieveAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.Product_By_CategorySerializer


class ListSocialNetwork(generics.ListAPIView):
    queryset = models.SocialNetworks.objects.all()
    serializer_class = serializer.SocialNetworkSerializer


class ListLocation(generics.ListAPIView):
    queryset = models.Location.objects.all()
    serializer_class = serializer.LocationSerializer


class List_UserData(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer


class DetailUserData(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializer.ProductSerializer


class ListDiscount(generics.ListCreateAPIView):
    queryset = models.Discount.objects.all()
    serializer_class = serializer.DiscountSerializer


class ListOrders(generics.ListCreateAPIView):
    queryset = models.Orders.objects.all()
    serializer_class = serializer.OrdersSerializer


class ListBestSeller(generics.ListAPIView):
    queryset = models.Best_seller_products.objects.filter(best_seller_product=True)
    serializer_class = serializer.BestSellerProductSerializer


class ListProductsByCategoryName(generics.ListAPIView):
    queryset = models.Product.objects.all().order_by('-id')
    serializer_class = serializer.Product_By_CategorySerializer

    def list(self, request, *args, **kwargs):
        cache_key = "products_by_category:all"
        data_all = cache.get(cache_key)
        if data_all is not None:
            # Group the data by category name and return it
            sorted_data = {}
            for item in data_all:
                category_name = item['category_name']
                if category_name not in sorted_data:
                    sorted_data[category_name] = []
                sorted_data[category_name].append(item)
            return Response(sorted_data)

        # Data is not available in cache, fetch it from API or database
        response = requests.get(url, auth=(username, password), params={'sort_by': '-id'})
        if response.status_code != 200:
            return Response({'error': 'Failed to fetch data from API'})

        # Process the data and create Product objects
        json_data = response.json()
        products_data = json_data.get('Товары', [])
        products = []
        for product_data in products_data:
            category_name = product_data.get('Категория', '').strip()
            if category_name:
                name_category = Category.objects.filter(name_ru=category_name)
                if name_category.exists():
                    category = name_category.first()
                else:
                    category = Category.objects.create(name_ru=category_name)
                product_name = product_data.get('Наименование')
                try:
                    category = Product.objects.get(name_ru=product_name, category=category)
                except ObjectDoesNotExist:
                    product = Product(name_ru=product_name,
                                      description_ru=product_data['Описание'],
                                      price=product_data['Цена'],
                                      category=category,
                                      code=product_data['Код'],
                                      count=product_data['Остаток'],
                                      image1=product_data.get('image1', 'None'),
                                      image2=product_data.get('image2', 'None'),
                                      image3=product_data.get('image3', 'None'),
                                      image4=product_data.get('image4', 'None'),
                                      image5=product_data.get('image5', 'None'),
                                      korzinka=product_data.get('korzinka', False),
                                      saralangan=product_data.get('saralangan', False),
                                      solishtirsh=product_data.get('solishtirsh', False),
                                      best_seller_product=product_data.get('best_seller_product', False))
                    products.append(product)
                except MultipleObjectsReturned:
                    pass

        # Bulk create the Product objects
        # products_sorted = sorted(products, key=lambda p: p.id, reverse=True)
        Product.objects.bulk_create(products)

        # Retrieve the Product queryset from the database and group the data by category name
        queryset = Product.objects.all().order_by('-id')
        sorted_data = {}
        for item in queryset:
            category_name = item.category.name_ru
            if category_name not in sorted_data:
                sorted_data[category_name] = []
            serializer_ = self.get_serializer(item)
            sorted_data[category_name].append(serializer_.data)

        # Store the serialized data in cache and return it
        cache.set(cache_key, sorted_data, timeout=settings.CACHE_TIME)
        return Response(sorted_data)


class ListProductsByCategoryNameNew(generics.ListAPIView):
    queryset = models.ProductNew.objects.all().order_by('-id')
    serializer_class = serializer.Product_By_CategorySerializer

    def list(self, request, *args, **kwargs):
        cache_key = "products_by_category:all_"
        data_all = cache.get(cache_key)
        if data_all is not None:
            # Group the data by category name and return it
            sorted_data = {}
            for item in data_all:
                category_name = item['category_name']
                if category_name not in sorted_data:
                    sorted_data[category_name] = []
                sorted_data[category_name].append(item)
            return Response(sorted_data)

        # Data is not available in cache, fetch it from API or database
        response = requests.get(url, auth=(username, password), params={'sort_by': '-id'})
        if response.status_code != 200:
            return Response({'error': 'Failed to fetch data from API'})

        # Process the data and create Product objects
        json_data = response.json()
        products_data = json_data.get('Товары', [])
        products = []
        for product_data in products_data:
            category_name = product_data.get('Категория', '').strip()
            if category_name:
                name_category = Category.objects.filter(name_ru=category_name)
                if name_category.exists():
                    category = name_category.first()
                else:
                    category = Category.objects.create(name_ru=category_name)
                product_name = product_data.get('Наименование')
                try:
                    category = Product.objects.get(name_ru=product_name, category=category)
                except ObjectDoesNotExist:
                    product = Product(name_ru=product_name,
                                      description_ru=product_data['Описание'],
                                      price=product_data['Цена'],
                                      category=category,
                                      code=product_data['Код'],
                                      count=product_data['Остаток'],
                                      image1=product_data.get('image1', 'None'),
                                      image2=product_data.get('image2', 'None'),
                                      image3=product_data.get('image3', 'None'),
                                      image4=product_data.get('image4', 'None'),
                                      image5=product_data.get('image5', 'None'),
                                      korzinka=product_data.get('korzinka', False),
                                      saralangan=product_data.get('saralangan', False),
                                      solishtirsh=product_data.get('solishtirsh', False),
                                      best_seller_product=product_data.get('best_seller_product', False))
                    products.append(product)
                except MultipleObjectsReturned:
                    pass

        # Bulk create the Product objects
        # products_sorted = sorted(products, key=lambda p: p.id, reverse=True)
        Product.objects.bulk_create(products)

        # Retrieve the Product queryset from the database and group the data by category name
        queryset = Product.objects.all().order_by('-id')
        sorted_data = {}
        for item in queryset:
            category_name = item.category.name_ru
            if category_name not in sorted_data:
                sorted_data[category_name] = []
            serializer_ = self.get_serializer(item)
            sorted_data[category_name].append(serializer_.data)

        # Store the serialized data in cache and return it
        cache.set(cache_key, sorted_data, timeout=settings.CACHE_TIME)
        return Response(sorted_data)


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer


class ChatMessageViewSet(viewsets.ModelViewSet):
    queryset = ChatMessage.objects.all()
    serializer_class = ChatMessageSerializer


class ListBaraban(generics.ListAPIView):
    queryset = models.BarabanDiscount.objects.all()
    serializer_class = serializer.BarabanDiscountSerializer


class ProductsByCategoryView(APIView):
    def get(self, request, *args, **kwargs):
        products = None
        category_name = kwargs.get('category_name')
        price_filter = kwargs.get('price')

        if category_name:
            try:
                category = Category.objects.get(name_en=category_name)
                products = category.product_set.all()
            except Category.DoesNotExist:
                return JsonResponse({'error': f'Category {category_name} does not exist.'}, status=404)
        else:
            products = Product.objects.all()

        if price_filter == 'max':
            products = products.filter(price__gte='2000000')
        elif price_filter == 'min':
            products = products.filter(price__lt='2000000')

        # group products by category
        categories_data = {}
        for product in products:
            category_name = product.category.name_ru
            if category_name not in categories_data:
                categories_data[category_name] = []
            categories_data[category_name].append({
                'name_uz': product.name_uz,
                'name_en': product.name_en,
                'name_ru': product.name_ru,
                'description_uz': product.description_uz,
                'description_en': product.description_en,
                'description_ru': product.description_ru,
                'count': product.count,
                'code': product.code,
                'price': str(product.price),
                'image1': product.image1.url if product.image1 else None,
                'image2': product.image2.url if product.image2 else None,
                'image3': product.image3.url if product.image3 else None,
                'image4': product.image4.url if product.image4 else None,
                'image5': product.image5.url if product.image5 else None,
                'korzinka': product.korzinka,
                'saralangan': product.saralangan,
                'solishtirsh': product.solishtirsh,
                'best_seller_product': product.best_seller_product,
            })

        return JsonResponse(categories_data, safe=False)


class ProductsByCategoryViewGetByCount(APIView):
    def get(self, request, *args, **kwargs):
        products = Product.objects.order_by('-id')
        categories_data = {}
        for product in products:
            category_name = product.category.name_ru
            if category_name not in categories_data:
                categories_data[category_name] = []
            if len(categories_data[category_name]) <= 4: # Changed to <= 4 to get 5 objects
                categories_data[category_name].append({
                    'name_uz': product.name_uz,
                    'name_en': product.name_en,
                    'name_ru': product.name_ru,
                    'description_uz': product.description_uz,
                    'description_en': product.description_en,
                    'description_ru': product.description_ru,
                    'count': product.count,
                    'code': product.code,
                    'price': product.price,
                    'image1': product.image1.url if product.image1 else None,
                    'image2': product.image2.url if product.image2 else None,
                    'image3': product.image3.url if product.image3 else None,
                    'image4': product.image4.url if product.image4 else None,
                    'image5': product.image5.url if product.image5 else None,
                    'korzinka': product.korzinka,
                    'saralangan': product.saralangan,
                    'solishtirsh': product.solishtirsh,
                    'best_seller_product': product.best_seller_product,
                })
            else:
                continue
        return JsonResponse(categories_data, safe=False)
