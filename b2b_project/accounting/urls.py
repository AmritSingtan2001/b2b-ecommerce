from django.urls import path

from .views import list_credits

app_name = 'accounting'
urlpatterns = [ 
    path('admin-dashboard/credits/', list_credits, name='list_credits'),
]