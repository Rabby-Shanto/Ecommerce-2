from django.contrib import admin

# Register your models here.
from .models import Product,Brand,Colour,Banner,ProductVaraiant,Size,ProductGallery
from easy_select2 import select2_modelform
import admin_thumbnails

prod_form =  select2_modelform(ProductVaraiant, attrs={'width': '250px'})

@admin_thumbnails.thumbnail('images')
class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1


class productAdmin(admin.ModelAdmin):
    
    list_display = ('product_name','price','category','is_available','img_preview')
    prepopulated_fields = {'slug':('product_name',)}
    inlines = [ProductGalleryInline]

class ProductVariantAdmin(admin.ModelAdmin):
    form = prod_form
    list_display = ('get_name','color','size','brand')
    search_fields = ('product__product_name','brand__title')

    def get_name(self,obj):
        return obj.product.product_name
    get_name.short_description = 'product_name'
    

    


admin.site.register(Product,productAdmin)
admin.site.register(Brand)
admin.site.register(Colour)
admin.site.register(Banner)
admin.site.register(ProductVaraiant,ProductVariantAdmin)
admin.site.register(Size)
admin.site.register(ProductGallery)




