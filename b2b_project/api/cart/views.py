from rest_framework.viewsets import ModelViewSet

from .models import Cart
from .serializers import CartSerializer

class CartViewSet(ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer