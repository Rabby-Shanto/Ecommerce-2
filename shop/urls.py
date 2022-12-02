from django.urls import path
from .import views


urlpatterns = [
    path('',views.shop,name='shop'),
    path('<slug:category_slug>/',views.shop,name="Category_products"),
    path('<slug:category_slug>/<slug:product_slug>/',views.product_detail,name="products_details"),
]
