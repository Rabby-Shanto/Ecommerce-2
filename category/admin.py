from django.contrib import admin

from .models import Category

# Register your models here.

@admin.register(Category)



class categoryAdmin(admin.ModelAdmin):

    prepopulated_fields = {'slug':('category_name',)}
    readonly_fields = ['img_preview']
    list_display = ['category_name','slug','img_preview']
