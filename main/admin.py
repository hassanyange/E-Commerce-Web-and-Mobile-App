from django.contrib import admin
from .models import UserProfile, Category, Invoice, Customer, Item, OrderItem, Cart, Address, Payment, Coupon, Refund, Comment, RawMaterial, BuildingSupply, ConstructionEquipment, ArchitecturalProduct

admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(Invoice)
admin.site.register(Payment)
admin.site.register(Customer)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Comment)
admin.site.register(RawMaterial)
admin.site.register(BuildingSupply)
admin.site.register(ConstructionEquipment)
admin.site.register(ArchitecturalProduct)
