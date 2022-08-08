from django.db.models.signals import post_save
from .models import Order
from orders.utils import send_mail_on_order

post_save.connect(send_mail_on_order, sender = Order)