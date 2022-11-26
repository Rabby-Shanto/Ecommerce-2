from django.db import models
from django.urls import reverse
from category.models import Category
from django.utils.html import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField

class Product(models.Model):
    product_name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=100,unique=True)
    content = RichTextUploadingField()
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    # def get_url(self):

    #     return reverse('products_details',args=[self.category.slug,self.slug])

    def __str__(self):
        return self.product_name

    def img_preview(self): 
        return mark_safe('<img src = "{url}" width = "50" height = "50"/>'.format(
             url = self.images.url
         ))


