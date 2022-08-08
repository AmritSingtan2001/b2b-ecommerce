from ast import mod
from distutils.command.upload import upload
from django.db import models



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
    logo = models.ImageField(upload_to ='brandimage/')

    def __str__(self):
        return self.name

class Product(models.Model):
    COLOR_CHOICES = [
        ('white', 'White'),
        ('black', 'Black'),
        ('grey', 'Grey'),
        ('silver', 'Silver'),
        ('golden', 'Golden'),
    ]
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = 'products', verbose_name="Category*")
    sub_category = models.ForeignKey(SubCategory, on_delete = models.CASCADE, related_name = 'products', verbose_name="Sub Category*")
    sub_sub_category = models.ForeignKey(SubSubCategory, on_delete = models.CASCADE, related_name = 'products', verbose_name="Sub Sub Category*")
    name = models.CharField('Product Name*',max_length = 500)
    brand = models.ForeignKey(Brand, on_delete = models.CASCADE, blank = True, null = True, related_name = 'products')
    image = models.FileField('Product Images*',upload_to = 'images/')
    color = models.CharField('Product Color*',max_length=100, choices = COLOR_CHOICES, blank = True, null = True)
    price = models.DecimalField('Price*',max_digits = 10,decimal_places = 2)
    discounted_price = models.DecimalField('Discounted Price',max_digits = 10, decimal_places = 2, blank = True, null = True)
    stock = models.PositiveIntegerField('Stock*')
    size = models.CharField(max_length = 10, blank = True, null = True)
    type = models.CharField('Product Type',max_length = 10, blank = True, null = True)
    discriptions = models.TextField()
    is_featured = models.BooleanField('Featured Product',default = False)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_date = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name

