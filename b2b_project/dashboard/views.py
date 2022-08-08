from functools import total_ordering
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.paginator import Paginator
from shop.models import Category, SubCategory, SubSubCategory, Product,Brand
from orders.models import Order, OrderItem
from .cart import  Cart

def base(request):
    category = Category.objects.all()
    return render(request,'dashboard/base.html', {'category':category, 'types':category[:4]})

def index(request):
    category = Category.objects.all()
    product = Product.objects.all()
    newproduct= Product.objects.all().order_by('-created_date')
    brand = Brand.objects.all().order_by('-id')
    return render(request, 'dashboard/index.html', {'category': category , 
                                                    'types':category[:4], 
                                                    'product':product,
                                                    'newpd':newproduct[:8],
                                                    'brand':brand[:6]
                                                    }
    )
    
def shop(request,pk):
    cata= Category.objects.all()
    cat= Category.objects.get(id = pk)
    product = Product.objects.filter(category=cat)

    p = Paginator(product,3)
    page_number = request.GET.get('page')
    datafinal = p.get_page(page_number)

    sub_cata = SubCategory.objects.filter(category= cat)
    # brand = Brand.objects.filter(id = pk)
    return render(request,'dashboard/shop-grid.html',{'product':datafinal ,
                                                    'cata': cata,
                                                    'catagories':cata[:4],
                                                    'sub':sub_cata,'type':cat}
    )

def sub_category(request, pk):
    cata= Category.objects.all()
    cat = SubCategory.objects.get(id=pk)
    data = cat.category
    product = Product.objects.filter(sub_category= cat)
    p = Paginator(product,3)
    page_number = request.GET.get('page')
    datafinal = p.get_page(page_number)
    sub_data = SubSubCategory.objects.filter(sub_category =cat)
    return render(request,'dashboard/categoryshop.html',{'product':datafinal ,
                                                        'cata': cata,
                                                        'catagories':cata[:4],
                                                        'sub':sub_data,
                                                        'type':cat,
                                                        'data':data}
    )
    

def subsubcartegory(request,pk):
    cata = Category.objects.all()
    cat = SubSubCategory.objects.get(id = pk)
    product = Product.objects.filter(sub_sub_category = cat)
    p = Paginator(product,3)
    page_number = request.GET.get('page')
    datafinal = p.get_page(page_number)
    data = cat.sub_category
    data1 =data.category
    sub_data = SubSubCategory.objects.filter(sub_category= data)
    return render(request,'dashboard/subsubcategory.html',{'product':datafinal ,
                                                            'cata': cata,
                                                            'catagories':cata[:4],
                                                            'sub':sub_data,
                                                            'type':cat,
                                                            'data':data,
                                                            'data1':data1}
    )



def login_registration(request):
    return render(request,'dashboard/login.html')

def related_product(request, pk):
    category = Category.objects.all()
    product = Product.objects.get(id = pk)
    cat = product.category
    brand = product.brand
    # print(brand)
    products = Product.objects.filter(category = cat)
    return render(request,'dashboard/shop-details.html',{'product':product,
                                                        'related_products':products[:6], 
                                                        'cata':category, 
                                                        'type':category[:4]}
    )
    

def showcart(request):
    cata= Category.objects.all()
    cart = Cart(request)
    carts = cart.List()
    total = cart.totalprice()
    gettotal = cart.get_total_price()
    return render(request,'dashboard/shoping-cart.html',{'category':cata,
                                                        'type':cata[:4], 
                                                        'cart':carts, 
                                                        'total':total, 
                                                        'gettotal':gettotal}
    )
    


def addtocart(request):
    if request.method == 'POST':
        id = request.POST.get('p_id')
        product = Product.objects.get(id = id)
        quantity = request.POST.get('quantity')
        if quantity == None:
            quantity = 1
        
        cart = Cart(request)
        cart.add(product, quantity)

        return showcart(request)
        
    else:
        return showcart(request)

def update(request):
    if request.method == 'POST':
        id = request.POST['p_id']
        quantity = request.POST['quantity']
        product = Product.objects.get(id = id)
        cart = Cart(request)
        cart.add(product, quantity, override_quantity= True)
        return showcart(request)
    else:
        return HttpResponse("Cannot update")


def delete(request, pk):
    product = Product.objects.get(id = pk)
    cart = Cart(request)
    cart.remove(product)
    return showcart(request)

@login_required
def checkout(request):
    cata= Category.objects.all()
    cart = Cart(request)
    total = cart.totalprice()
    carts_data = cart.List()
    grandtotal = cart.get_total_price()
    return render(request,'dashboard/checkout.html',{'category':cata,
                                                    'type':cata[:4], 
                                                    'carts':carts_data, 
                                                    'total':total, 
                                                    'grandtotal':grandtotal}
    )

def about(request):
    cata= Category.objects.all()
    return render(request,'dashboard/about.html',{'category':cata, 'cata':cata[:4]})

def contact(request):
    cata= Category.objects.all()
    return render(request,'dashboard/contact.html',{'category':cata,'type':cata[:4]})

def blog(request):
    cata= Category.objects.all()
    return render(request,'dashboard/blog.html',{'category':cata,'type':cata[:4]} )

def brand(request, pk):
    cata= Category.objects.all()
    brand = Brand.objects.get(id= pk)
    product = Product.objects.filter(brand= brand)
    others = Brand.objects.all()
    return render(request, 'dashboard/brandshop.html',{'cata':cata,
                                                        'type':cata,
                                                        'catagories':cata[:4],
                                                        'product':product,
                                                        'brand':brand, 
                                                        'otherbrand':others}
    )

@login_required
def orderplace(request):
    cart = Cart(request)
    carts = cart.List()
    if request.method=="POST":
        method = request.POST.get('cod')
        user = request.user
        order = Order.objects.create(user= user, payment_method = method)
        order.save()
        for i in carts:
            OrderItem.objects.create(order= order, product = i['obj'], quantity = i['quantity'])
            product = Product.objects.get(id = i['id'])
            quantity = i['quantity']
            stk = product.stock
            stock1 = stk - int(quantity)
            product.stock =  stock1
            product.save()
            cart.remove(product)
        
        return index(request)
        
    else:
        return checkout(request)

def logout_account(request):
    logout(request)
    return index(request)


def search(request):
    cata = Category.objects.all()
    query = request.GET['query']
    subdata= None
    data = Product.objects.filter(name__icontains = query)
    if data:
        return render(request, 'dashboard/search.html', {'data':data,
                                                        'cata':cata, 
                                                        'cat':cata[:4]}
        )
    else:
        return render(request, 'dashboard/search.html', {'data':data,
                                                        'cata':cata, 
                                                        'cat':cata[:4], 
                                                        'subdata':subdata}
        )