from django.contrib import admin
from django.urls import path, include

from rest_api.urls import router



urlpatterns = [
    path('api/', include('rest_api.urls')),
    # path('api/v2/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
]
