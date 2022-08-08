from rest_framework import serializers

from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.HyperlinkedRelatedField(many = False, read_only = True, view_name = 'product-detail')
    class Meta:
        model = OrderItem
        fields = ['id', 'order', 'product', 'quantity', 'get_cost']

class OrderSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name = 'order-detail', many = True, read_only = True)
    items = OrderItemSerializer(many = True, read_only = True)
    class Meta:
        model = Order
        fields = ['id', 'user','payment_method', 'order_status', 'get_total_cost','created', 'updated', 'items']