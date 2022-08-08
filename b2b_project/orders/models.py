from django.db import models

from user.models import User
from shop.models import Product


class OrderQuerySet(models.QuerySet):
    def get_revenue(self, start_date, end_date):
        return sum([order.get_total_cost() for order in Order.objects.filter(created__range = [start_date, end_date])])


class OrderManager(models.Manager):
    def get_queryset(self):
        return OrderQuerySet(self.model, using=self._db)


class Order(models.Model):
    PAYMENT_CHOICES = [('Credit', 'Credit'),('Cash on Delivery', 'Cash on Delivery')]
    ORDER_STATUS_CHOICES = [('unverified', 'Unverified'),
                            ('verified','Verified'),
                            ('on_delivery', 'On Delivery'),
                            ('delivered', 'Delivered'),
                            ('cancelled','Cancelled')]

    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'orders')
    payment_method = models.CharField(max_length = 50, choices = PAYMENT_CHOICES)
    order_status = models.CharField(max_length = 50, choices = ORDER_STATUS_CHOICES, default='unverified')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)
    objects = OrderManager()

    class Meta:
        ordering = ['-created']
        
    def __str__(self):
        return f"Order {self.id}"
    
    def get_total_cost(self):
        return sum([item.get_cost() for item in self.items.all()]) 

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete = models.CASCADE, related_name = 'items')
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    #price = models.DecimalField(decimal_places = 2,max_digits = 10)
    quantity = models.PositiveIntegerField(default = 1)

    def __str__(self):
        return f"{self.id}"
    
    def get_cost(self):
        if self.product.discounted_price:
            return self.product.discounted_price * self.quantity
        
        else:
            return self.product.price * self.quantity

