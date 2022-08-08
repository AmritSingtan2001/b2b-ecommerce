from django.db import models
from shop.models import Product
from user.models import User

class Cart(models.Model):
    customer = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'cart')

    def get_total_cost(self):
        return sum([item.get_cost() for item in self.items.all()])

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, related_name = 'items')
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField()

    def get_cost(self):
        return self.product.price * self.quantity