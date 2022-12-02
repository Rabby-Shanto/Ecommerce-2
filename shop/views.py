from django.shortcuts import render,get_object_or_404
from category.models import Category
from .models import Product,ProductVaraiant,Colour,ProductGallery



# Create your views here.

def shop(request,category_slug=None):

    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category,slug = category_slug)
        products = Product.objects.filter(category=categories,is_available=True).order_by('id')
        variation = ProductVaraiant.objects.filter(product__category=categories).values('color__title').distinct()
        products_count = products.count()
        
    else:
        products = Product.objects.all().filter(is_available=True).order_by('id')
        products_count = products.count()
        variation = ProductVaraiant.objects.all().values('color__title').distinct()

    context = {
        'products' : products,
        'products_count' : products_count,
        'variation' : variation,
        # 'colors' : colors
    }
    return render(request,'shop/shop.html',context)

def product_detail(request,category_slug,product_slug):
    single_product = Product.objects.get(category__slug=category_slug,slug=product_slug)
    variation_colors = ProductVaraiant.objects.filter(product = single_product,product__is_available=True).values('color__title').distinct()
    product_gallery = ProductGallery.objects.filter(product_id=single_product.id)
    context = {
        'single_product' : single_product,
        'product_gallery' : product_gallery,
        'variation_colors' : variation_colors
    }
    return render(request,"shop/detail.html",context)


