from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from orders.models import Order

def send_mail_on_order(sender, instance, **kwargs):
    order = instance
    subject = 'Order Placed Successfully'
    message = render_to_string('orders/invoice_template.html', {'order':order})
    email = EmailMessage(subject, message, 'sumangaire52@gmail.com', [order.user.email])
    email.content_subtype = 'html'
    email.send()