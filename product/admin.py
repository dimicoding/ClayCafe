from django.contrib import admin
from .models import Product, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    """
    Categories admin panel
    """
    list_display = (
        'cat_name',
    )
    
class ProductAdmin(admin.ModelAdmin):
    """
    Products admin panel
    """
    list_display = (
        'name',
        'description',
        'price',
        'image',
        'category',
    )
    ordering = ('-id',)




admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)

