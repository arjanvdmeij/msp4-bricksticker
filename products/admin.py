from django.contrib import admin
from .models import Product, ProductComment


class ProductCommentInline(admin.TabularInline):
    model = ProductComment

    
class ProductAdmin(admin.ModelAdmin):
    inlines = (ProductCommentInline, )
    
admin.site.register(Product, ProductAdmin)
