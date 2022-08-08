from django.shortcuts import redirect, render, get_object_or_404

from .models import Order

def new_orders(request):
    new_orders = Order.objects.filter(order_status = 'unverified')
    return render(request,'orders/new_orders.html', {'new_orders':new_orders})

def verify_order(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    order.order_status = 'verified'
    order.save()
    return redirect('orders:new_orders')

def verified_orders(request):
    verified_orders = Order.objects.filter(order_status = 'verified')
    return render(request, 'orders/verified_orders.html', {'verified_orders':verified_orders})

def mark_order_on_delivery(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    order.order_status = 'on_delivery'
    order.save()
    return redirect('orders:verified_orders')

def orders_on_delivery(request):
    on_delivery_orders = Order.objects.filter(order_status = 'on_delivery')
    return render(request, 'orders/on_delivery.html', {'on_delivery_orders':on_delivery_orders})

def mark_order_completed(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    order.order_status = 'delivered'
    order.save()
    return redirect('orders:orders_on_delivery')

def completed_orders(request):
    completed_orders = Order.objects.filter(order_status = 'delivered')
    return render(request,'orders/completed_orders.html', {'completed_orders':completed_orders})

def cancelled_orders(request):
    cancelled_orders = Order.objects.filter(order_status = 'cancelled')
    return render(request,'orders/cancelled_orders.html', {'cancelled_orders':cancelled_orders})

def order_invoice(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    return render(request, 'orders/invoice.html', {'order':order})