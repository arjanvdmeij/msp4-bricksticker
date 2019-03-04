from django.contrib import admin
from .models import Order, OrderItem


class OrderAdminInline(admin.TabularInline):
    model = OrderItem

""" Group items ordered within the Order
"""    
class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderAdminInline, )
    
admin.site.register(Order, OrderAdmin)