from django.urls import path, include

urlpatterns = [
    path('users/', include('user.urls')),
    path('products/', include('shop.urls')),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
]