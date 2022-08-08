from django.db import models
from user.models import Customer

class Credit(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='credits')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.customer.full_name