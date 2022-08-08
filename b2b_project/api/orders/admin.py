from django.contrib import admin

from .models import Order, OrderItem

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields: ['product']

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_filter = ['payment_method', 'order_status']
    
admin.site.register(Order, OrderAdmin)