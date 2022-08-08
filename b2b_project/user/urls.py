from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [ 
    path('signup/', views.CustomerSignupView.as_view(), name = 'customer_signup'),
    path('salesman-signup/', views.SalesmanSignupView.as_view(), name = 'salesman_signup')
]