from rest_framework.routers import DefaultRouter

from apps.products import views

router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='category')
router.register(r'', views.ProductViewSet, basename='product')

urlpatterns = router.urls
