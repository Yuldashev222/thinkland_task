from django.contrib import admin

from apps.products.models import Product, Category

admin.site.register([Product, Category])
