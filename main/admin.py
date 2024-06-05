from django.contrib import admin
from .models import  Category, Invoice, Customer, Item, OrderItem, Cart, Address, Payment, Order

admin.site.register(Category)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(Customer)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'product_name', 'status', 'estimated_delivery_date')
    list_filter = ('status',)
    search_fields = ('customer_name', 'product_name')
    ordering = ('-estimated_delivery_date',)

admin.site.register(Order, OrderAdmin)