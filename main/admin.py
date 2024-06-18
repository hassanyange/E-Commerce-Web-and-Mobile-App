from django.contrib import admin
from .models import Order, Invoice, Payment, Comment, Customer, Category, Item, Address

admin.site.register(Order)
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(Comment)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Address)
