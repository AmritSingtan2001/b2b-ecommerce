from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [ 
    path('', views.index, name= 'index'),
    path('related/<int:pk>', views.related_product, name = 'related'),
    path('shop<int:pk>', views.shop,name='shop'),
    path('addto', views.addtocart, name='addto'),
    path('checkout', views.checkout, name='checkout'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('brand<int:pk>', views.brand, name='brand'),
    path('update', views.update, name='update'),
    path('delete<int:pk>', views.delete, name='delete'),
    path('show', views.showcart, name='show'),
    path('order', views.orderplace, name='order'),
    path('logout', views.logout_account, name='logout'),
    path('subsub/<int:pk>', views.sub_category, name='subsub'),
    path('subsubcategory/<int:pk>', views.subsubcartegory, name='subsubcategory'),
    path('search', views.search, name='search'),
]