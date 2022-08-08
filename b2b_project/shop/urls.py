from django.urls import path

from . import views


app_name = 'shop'

urlpatterns = [ 
    path('', views.home, name = 'home'),
    path('admin-dashboard/', views.admin_dashboard, name = 'admin_dashboard'),
    path('admin-dashboard/profile/', views.admin_profile, name = 'admin_profile'),
    path('admin-dashboard/profile/<str:edit>/', views.admin_profile, name = 'admin_profile_edit'),
    path('admin-dashboard/product-list/', views.product_list, name = 'product_list'),
    path('admin-dashboard/product/<int:id>/', views.product_detail, name = 'product_detail'),
    path('admin-dashboard/add-product/', views.add_product, name = 'add_product'),
    path('admin-dashboard/customer-list/', views.list_customer, name = 'customer_list'),
    path('admin-dashboard/customer-list/<int:user_id>/block/', views.block_customer, name = 'block_customer'),
    path('admin-dashboard/customer-requests/', views.customer_requests, name = 'customer_requests'),
    path('admin-dashboard/customer-requests/<int:user_id>/remove/', views.remove_customer, name = 'remove_customer'),
    path('admin-dashboard/customer-requests/<int:user_id>/approve/', views.approve_customer, name = 'approve_customer'),
    path('admin-dashboard/salesman-list/', views.list_salesman, name = 'salesman_list'),
    path('admin-dashboard/salesman-requests/', views.salesman_requests, name = 'salesman_requests'),
    path('admin-dashboard/salesman-requests/<int:user_id>/remove/', views.remove_salesman, name = 'remove_salesman'),
    path('admin-dashboard/salesman-requests/<int:user_id>/approve/', views.approve_salesman, name = 'approve_salesman'),
    path('admin-dashboard/customer-list/<int:user_id>/block/', views.block_salesman, name = 'block_salesman'),
]