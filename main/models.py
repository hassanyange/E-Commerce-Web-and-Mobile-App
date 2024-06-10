from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('Roofing Materials', 'Roofing Materials'),
    ('Structural materials', 'Structural materials'),
    ('Plumbing and Electrical Materials', 'Plumbing and Electrical Materials')
)






class Customer(models.Model):
    username = models.CharField(max_length=255, blank=True)
    email = models.EmailField(default="customer@gmail.com")
    location = models.CharField(max_length=200, default="Dar es salaam")
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.username


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category



class Item(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    item_image = models.ImageField(upload_to='items_images/')
    description = models.TextField()
    seller_name = models.CharField(max_length=100, default="john")

    def __str__(self):
        return self.item_name

   

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    billing_address = models.ForeignKey('Address', related_name='billing_address', on_delete=models.SET_NULL, blank=True, null=True)
    shipping_address = models.ForeignKey('Address', related_name='shipping_address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', models.SET_NULL, blank=True, null=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = sum([item.item.price * item.quantity for item in self.items.all()])
        return total

class Order(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Order Confirmation'),
        ('shipped', 'Order Shipment'),
        ('estimated_delivery', 'Estimated Delivery Time'),
        ('delivered', 'Delivery Update Feedback Request'),
    ]

    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    estimated_delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product_name} for {self.customer_name}"
    
class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1,)
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

class Invoice(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    order = models.OneToOneField(Cart, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Invoice {self.id} for {self.user.username}"

class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    successful = models.BooleanField(default=False)

    def __str__(self):
        return f"Payment {self.id} by {self.user.username}"



class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment


# models.py
from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [
        ('confirmed', 'Order Confirmation'),
        ('shipped', 'Order Shipment'),
        ('estimated_delivery', 'Estimated Delivery Time'),
        ('delivered', 'Delivery Update Feedback Request'),
    ]

    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='confirmed')
    estimated_delivery_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.product_name} for {self.customer_name}"



# Signal to create user profile every time a new user is created


