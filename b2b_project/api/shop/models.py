from django.db import models

from colorfield.fields import ColorField

class Category(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'

class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Sub Categories'

class SubSubCategory(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete = models.CASCADE)
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Sub Sub Categories'

class Brand(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name

class Product(models.Model):
    COLOR_CHOICES = [
        ('#FFFFFF', 'White'),
        ('##000000', 'Black'),
        ('#808080', 'Grey'),
        ('#C0C0C0', 'Silver'),
        ('#FFD700', 'Golden'),
    ]
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'products')
    sub_category = models.ForeignKey(SubCategory, on_delete = models.Model, related_name = 'products')
    sub_sub_category = models.ForeignKey(SubSubCategory, on_delete = models.CASCADE, related_name = 'products')
    name = models.CharField(max_length = 500)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, blank = True, null = True, related_name = 'products')
    image = models.FileField(upload_to = 'images/')
    color = ColorField(choices = COLOR_CHOICES, blank = True, null = True)
    price = models.DecimalField(max_digits = 10,decimal_places = 2)
    discounted_price = models.DecimalField(max_digits = 10, decimal_places = 2, blank = True, null = True)
    stock = models.PositiveIntegerField()
    size = models.CharField(max_length = 10, blank = True, null = True)
    type = models.CharField(max_length = 10, blank = True, null = True)
    is_featured = models.BooleanField(default = False)

    def __str__(self):
        return self.name

