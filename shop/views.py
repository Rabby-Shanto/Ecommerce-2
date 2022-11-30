from django.shortcuts import render,get_object_or_404
from category.models import Category
from .models import Product,ProductVaraiant



# Create your views here.

def shop(request,category_slug=None):

    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category,slug = category_slug)
        products = Product.objects.filter(category=categories,is_available=True).order_by('id')
        variation = ProductVaraiant.objects.filter(product__category = categories)
        print(variation)
        products_count = products.count()
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        products_count = products.count()
        variation = ProductVaraiant.objects.all()
        print(variation)

    context = {
        'products' : products,
        'products_count' : products_count,
        'variation' : variation
    }
    return render(request,'shop/shop.html',context)


