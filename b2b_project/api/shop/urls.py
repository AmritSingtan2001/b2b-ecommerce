from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (BrandViewSet, 
                    CategoryViewSet, 
                    SubCategoryViewSet, 
                    SubSubCategoryViewSet, 
                    ProductViewSet)

router = SimpleRouter()
router.register('category', CategoryViewSet)
router.register('sub-category', SubCategoryViewSet)
router.register('sub-sub-category', SubSubCategoryViewSet)
router.register('brand', BrandViewSet)
router.register('', ProductViewSet)

urlpatterns = [
    path('', include(router.urls)),
]