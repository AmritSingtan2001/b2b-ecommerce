from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import OrderViewSet, OrderItemViewSet

router = SimpleRouter()
router.register('', OrderViewSet, basename = 'orders')
router.register('items/', OrderItemViewSet, basename = 'order_items')

urlpatterns = [ 
    path('', include(router.urls)),
]