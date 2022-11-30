from django.shortcuts import render

from shop.models import Product



def home(request):
    products = Product.objects.all().filter(is_available=True,is_featured=True)

    context = {
        'products' : products,
    }
    return render(request,'index.html',context)