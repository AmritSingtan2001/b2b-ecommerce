from unicodedata import category
from shop.models import Category, SubCategory, SubSubCategory, Product,Brand

def all_category(request):
    category = Category.objects.all()
    return({'cata':category})

def producttypes(request):
    types = Category.objects.all()
    return({'category':types[:4]})

