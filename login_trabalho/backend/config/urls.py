
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from accounts.viewsets import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path(r'api/v1/', include(router.urls)),

]
