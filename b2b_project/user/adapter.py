from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class CustomAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):

        assert request.user.is_authenticated
        
        if request.user.is_admin:
            url = 'shop:admin_dashboard'
        
        if request.user.is_customer:
            url = 'shop:home'

        return reverse(url)