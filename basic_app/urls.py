from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from basic_app import views
from basic_app.views import BestSellerProductsList1, ListHeaderCarousel

urlpatterns = [
    path('gallery/', views.ListGalleryData1.as_view()),
    path('gallery/<int:pk>', views.DetailGalleryData1.as_view()),
    path('photos/', views.ListGalleryPhotos1.as_view()),
    path('photos/<int:pk>', views.DetailGalleryPhotos1.as_view()),
    path('form/', views.ListForm.as_view()),
    path('about/', views.ListAbout.as_view()),
    path('gallery_images/', views.ListGalleryOnlyImages.as_view()),
    path('infografika/', views.ListInfoGrafika.as_view()),
    path('partners/', views.ListPartners.as_view()),
    path('gallery_news/', views.ListGalleryNews.as_view()),
    path('gallery_news/<int:pk>', views.DetailGalleryNews.as_view()),
    path('social_networks/', views.ListSocialNetwork.as_view()),
    path('category/', views.ListCategory.as_view()),
    path('works_kale/', views.ListWorksByKale.as_view()),
    path('location/', views.ListLocation.as_view()),
    path('sub_category_products/', views.ListSubCategory.as_view()),
    path('header/', ListHeaderCarousel.as_view(), name='header_carousel_list'),
    path('best_seller/count=<int:count>/', BestSellerProductsList1.as_view(), name='best_seller_products_count'),
    path('products_search/', views.ProductSearch.as_view()),
    path('products_by_category/<int:pk>/', views.DetailProductsByCategory1.as_view()),
    # path('products_by_category/', views.ListProductsByCategory1.as_view()),
    path('products_by_category/', views.ListProductsByCategory122.as_view()),
    path('orders/', views.ListOrders.as_view()),
    path('discount/', views.ListDiscount.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
