from django.db import models
from django.urls import reverse
from category.models import Category
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField


class Colour(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.title

class Size(models.Model):
    CHOICES = [
    ('Small', 'S'),
    ('Medium', 'M'),
    ('Large', 'L'),
    ('Extra large', 'XL'),
    ('Double Extra Large', 'XXL'),
]
    title = models.CharField(max_length=50,choices=CHOICES)

    def __str__(self):
        return self.title

class Brand(models.Model):
    title = models.CharField(max_length=100)
    brand_img = models.ImageField(upload_to='photos/brands')

    def __str__(self):
        return self.title


class Product(models.Model):
    product_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    content = RichTextUploadingField()
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_featured = models.BooleanField()


    # def get_url(self):

    #     return reverse('products_details',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.product_name

    def img_preview(self): 
        return mark_safe('<img src = "{url}" width = "50" height = "50"/>'.format(
             url = self.images.url
         ))

class Banner(models.Model):
    title = models.CharField(max_length=200)
    images = models.ImageField(upload_to='photos/banners')
    def __str__(self):
        return self.title



class ProductVaraiant(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    color = models.ForeignKey(Colour,on_delete=models.CASCADE,blank=True, null=True)
    size = models.ForeignKey(Size, on_delete=models.CASCADE,blank=True, null=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,blank=True, null=True)
    amount_in_stock = models.IntegerField()

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['product', 'color', 'size','brand'],
                name='unique_prod_color_size_combo'
            )
        ]

    def __str__(self):
        return self.product.product_name



