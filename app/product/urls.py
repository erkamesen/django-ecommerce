from django.urls import path, include
from rest_framework.routers import DefaultRouter
from product import views
router = DefaultRouter()

router.register("category", views.CategoryView)
router.register("brand", views.BrandView)
router.register("product", views.ProductView)


urlpatterns = [
    path('', include(router.urls)),
]
