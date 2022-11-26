from django.db import models
from django.urls import reverse
from django.utils.html import mark_safe

# Create your models here.


class Category(models.Model):
    parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    category_name = models.CharField(max_length=200,unique=True)
    category_img = models.ImageField(upload_to='photos/categories',blank=True)
    slug = models.SlugField(max_length=100,unique=True)
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def img_preview(self): 
        return mark_safe('<img src = "{url}" width = "50" height = "50"/>'.format(
             url = self.category_img.url
         ))

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name_plural = 'categories'
