from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('admin-dashboard/orders/new/', views.new_orders, name = 'new_orders'),
    path('admin-dashboard/orders/new/<int:order_id>/verify/', views.verify_order, name = 'verify_order'),
    path('admin-dashboard/orders/verified/', views.verified_orders, name = 'verified_orders'),
    path('admin-dashboard/orders/verified/<int:order_id>/mark_on_delivery/', views.mark_order_on_delivery, name = 'mark_on_delivery'),
    path('admin-dashboard/orders/on_delivery/', views.orders_on_delivery, name = 'orders_on_delivery'),
    path('admin-dashboard/orders/completed/', views.completed_orders, name = 'completed_orders'),
    path('admin-dashboard/orders/on_delivery/<int:order_id>/mark_completed/', views.mark_order_completed, name = 'mark_completed'),
    path('admin-dashboard/orders/cancelled/', views.cancelled_orders, name = 'cancelled_orders'),
    path('admin-dashboard/orders/<int:order_id>/invoice/', views.order_invoice, name = 'order_invoice'),   
]