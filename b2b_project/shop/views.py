import math
from datetime import timedelta, date
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from allauth.account.forms import ChangePasswordForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from orders.models import Order
from user.models import User
from .models import Product
from .decorators import admin_required
from .forms import AdminProfileEditform, AddProductForm
from .utils import (get_customer_report, 
                    get_revenue_report,
                    get_sales_report,
                    get_top_selling_product)


def home(request):
    return render(request, 'shop/home.html')


@login_required
@admin_required
def admin_dashboard(request):
    end_date = date.today() + timedelta(days=1)
    #get total orders of desired date range 
    order_duration = request.GET.get('duration', '1')
    start_date = date.today() - timedelta(days = int(order_duration))
    order_count = Order.objects.filter(created__range=[start_date, end_date]).count()
    previous_order_count = Order.objects.filter(created__range = [start_date, date.today()]).count()
    
    if previous_order_count > 0:
        percent_change = (order_count-previous_order_count)/previous_order_count*100
    else:
        percent_change = None

    #get total orders of desired date range
    revenue_duration = request.GET.get('revenue_duration', '1')
    revenue_start_date = date.today() - timedelta(days = int(revenue_duration))
    revenue = Order.objects.all().get_revenue(revenue_start_date, end_date)
    previous_revenue = Order.objects.all().get_revenue(revenue_start_date, date.today())

    if previous_revenue > 0:
        revenue_percent_change = math.floor(((revenue-previous_revenue)/previous_revenue*100))
    else:
        revenue_percent_change = None
    
     #get total orders of desired date range
    customer_duration = request.GET.get('customer_duration','1')
    customer_start_date = date.today() - timedelta(int(customer_duration))
    customer_count = User.objects.filter(is_customer = True, date_joined__range=[customer_start_date, end_date]).count()
    previous_customer_count = User.objects.filter(is_customer = True, date_joined__range = [customer_start_date, date.today()]).count()

    if previous_customer_count > 0:
        customer_percent_change = (customer_count - previous_customer_count)/previous_customer_count*100
    else:
        customer_percent_change = None
    
    report_timeframe = int(request.GET.get('report',7))
    #get the visualized report of sales, customers and revenue using apexchart.js
    dates = list(get_sales_report(report_timeframe).keys())
    dates.reverse()
    revenue_report = list(get_revenue_report(report_timeframe).values())
    revenue_report.reverse()
    customer_report = list(get_customer_report(report_timeframe).values())
    customer_report.reverse()
    sales_report = list(get_sales_report(report_timeframe).values())
    sales_report.reverse()
    recent_orders = Order.objects.all()[:50]
    top_selling_timeframe = int(request.GET.get('timeframe',1))
    top_selling_products = get_top_selling_product(top_selling_timeframe)

    return render(request, 'shop/admin_dashboard.html', {'order_count':order_count,
                                                         'filter_order_by':int(order_duration),
                                                         'percent_change':percent_change,
                                                         'revenue':revenue,
                                                         'revenue_duration':int(revenue_duration),
                                                         'revenue_percent_change':revenue_percent_change,
                                                         'customer_count':customer_count,
                                                         'customer_duration':int(customer_duration),
                                                         'customer_percent_change':customer_percent_change,
                                                         'dates':dates,
                                                         'revenue_report':revenue_report,
                                                         'customer_report':customer_report,
                                                         'sales_report':sales_report,
                                                         'recent_orders':recent_orders,
                                                         'top_selling_products':top_selling_products,
                                                         'top_selling_timeframe':top_selling_timeframe,})


@login_required
@admin_required
def admin_profile(request, edit = None, change_password = None):
    change_password_form = ChangePasswordForm()
    if edit == 'edit':
        if request.method == 'POST':
            admin_edit_form = AdminProfileEditform(request.POST)

            if admin_edit_form.is_valid():
                request.user.admin.full_name = admin_edit_form.cleaned_data['full_name']
                request.user.admin.address = admin_edit_form.cleaned_data['address']
                request.user.admin.contact_no = admin_edit_form.cleaned_data['contact_no']
                request.user.admin.save()
                return redirect('shop:admin_profile')

    return render(request, 'shop/admin_profile.html', {'change_password_form':change_password_form})


@login_required
@admin_required
def product_list(request):
    products = Product.objects.all()
    page = request.GET.get('page', 1)
    per_page = request.GET.get('per_page',100)
    paginator = Paginator(products, per_page)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    return render(request, 'shop/product_list.html', {'products':products})


@login_required
@admin_required
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shop:product_list')
    else:
        form = AddProductForm()
    return render(request, 'shop/add_product.html', {'form':form})


@login_required
@admin_required
def product_detail(request, id):
    product = get_object_or_404(Product, id = 1)
    return render(request,'shop/product_detail.html', {'product':product})


@login_required
@admin_required
def list_customer(request):
    customers = User.objects.filter(is_customer = True, is_active = True)
    return render(request, 'shop/customer_list.html', {'customers':customers})


@login_required
@admin_required
def block_customer(request,user_id):
    customer = get_object_or_404(User, id = user_id)
    customer.is_active = False
    customer.save()
    return redirect('shop:customer_list')


@login_required
@admin_required
def customer_requests(request):
    customer_requests = User.objects.filter(is_customer = True, is_active = False)
    return render(request, 'shop/customer_requests.html', {'customer_requests':customer_requests})


@login_required
@admin_required
def approve_customer(request, user_id):
    customer = get_object_or_404(User, id = user_id)
    customer.is_active = True
    customer.save()
    return redirect('shop:customer_requests')


@login_required
@admin_required
def remove_customer(request, user_id):
    customer = get_object_or_404(User, id = user_id)
    customer.delete()
    return redirect('shop:customer_requests')


@login_required
@admin_required
def salesman_requests(request):
    salesman_requests = User.objects.filter(is_salesman = True, is_active = False)
    return render(request, 'shop/salesman_requests.html', {'salesman_requests':salesman_requests})


@login_required
@admin_required
def approve_salesman(request, user_id):
    customer = get_object_or_404(User, id = user_id)
    customer.is_active = True
    customer.save()
    return redirect('shop:salesman_requests')


@login_required
@admin_required
def remove_salesman(request, user_id):
    customer = get_object_or_404(User, id = user_id)
    customer.delete()
    return redirect('shop:salesman_requests')


@login_required
@admin_required
def list_salesman(request):
    salesmen = User.objects.filter(is_salesman = True, is_active = True)
    return render(request, 'shop/salesman_list.html', {'salesmen':salesmen})


@login_required
@admin_required
def block_salesman(request,user_id):
    salesman = get_object_or_404(User, id = user_id)
    salesman.is_active = False
    salesman.save()
    return redirect('shop:salesman_list')