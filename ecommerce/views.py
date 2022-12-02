from django.shortcuts import render

from shop.models import Product
from category.models import Category
from django.db.models import F



def home(request):
    products = Product.objects.all().filter(is_available=True).order_by('-created_date')[:8]
    featured_product = Product.objects.all().filter(is_available=True,is_featured=True).order_by('-created_date')
    categories = Category.objects.filter(lft=F('rght')-1) #to get leaf node from django-mptt model
    print(categories)


    context = {
        'products' : products,
        'featured_product' : featured_product,
        'categories': categories,
    }
    return render(request,'index.html',context)