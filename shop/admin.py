from django.contrib import admin

# Register your models here.
from .models import Product




class productAdmin(admin.ModelAdmin):
    
    list_display = ('product_name','price','category','stock','is_available','img_preview')
    prepopulated_fields = {'slug':('product_name',)}

admin.site.register(Product,productAdmin)


