from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions, routers
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from basic_app.views import ChatRoomViewSet, ChatMessageViewSet

router = routers.DefaultRouter()
router.register('chatrooms/', ChatRoomViewSet)
router.register('chatmessages/', ChatMessageViewSet)
schema_view = get_schema_view(
    openapi.Info(
        title="Kale application programming interface",
        default_version='v1',
        description="Kale API",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path(settings.ADMIN_URL, admin.site.urls),
    path('', include('basic_app.urls')),
    # path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/', include(router.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

