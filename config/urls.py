"""
URL configuration for thinkland_task project.
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from .yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('auth/', include('apps.authentication.urls')),
    path('products/', include('apps.products.urls')),

    # swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
