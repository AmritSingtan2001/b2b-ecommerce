from orders.models import Order
from user.models import User
#from django.utils import timezone
from datetime import timedelta, date

def get_sales_report(date_range):
    order_data = {}
    for x in range(date_range):
        orders_for_day = Order.objects.filter(created__date = date.today()-timedelta(days = x)).count()
        order_data[str(date.today()-timedelta(days = x))] = orders_for_day
    
    return order_data


def get_revenue_report(date_range):
    revenue_data = {}
    for x in range(date_range):
        revenue_for_day = float(sum([order.get_total_cost() for order in Order.objects.filter(created__date = date.today()-timedelta(days = x))]))/10000
        revenue_data[str(date.today()-timedelta(days = x))] = revenue_for_day
    
    return revenue_data


def get_customer_report(date_range):
    customer_data = {}
    for x in range(date_range):
        customers_for_day = User.objects.filter(is_customer = True, date_joined__date = date.today()-timedelta(days = x)).count()
        customer_data[str(date.today()-timedelta(days = x))] = customers_for_day
    
    return customer_data

def get_top_selling_product(date_range):
    order_data = {}
    sorted_order_data = {}
    orders = Order.objects.filter(created__range = [date.today()-timedelta(days = date_range), date.today()+timedelta(days = 1)])

    for order in orders:
        for item in order.items.all():
            if item.product not in order_data:
                order_data[item.product] = item.quantity
            else:
                order_data[item.product] += item.quantity

    sorted_keys = sorted(order_data, key=order_data.get, reverse=True)

    for k in sorted_keys:
        sorted_order_data[k] = order_data[k]
    
    return sorted_order_data
    
    