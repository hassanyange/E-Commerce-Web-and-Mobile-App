from django.db import models
from django.db.models.signals import post_save
from django.conf import settings
from django.shortcuts import reverse
from django.contrib.auth.models import User

LABEL_CHOICES = (
    ('P', 'Primary'),
    ('S', 'Secondary'),
    ('D', 'Danger')
)

ADDRESS_CHOICES = (
    ('B', 'Billing'),
    ('S', 'Shipping')
)

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    stripe_customer_id = models.CharField(max_length=20, blank=True, null=True)
    on_click_purchasing = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username

class Customer(models.Model):
    name = models.CharField(max_length=255, blank=True)
    email = models.EmailField(default="customer@gmail.com")
    location = models.CharField(max_length=200, default="Dar es salaam")
    picture = models.ImageField(upload_to='static/images/', default='default.jpg')
    phone_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    category = models.CharField(max_length=30)

    def __str__(self):
        return self.category



class Item(models.Model):
    item_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    item_image = models.ImageField(upload_to='items_images/')
    labels = models.CharField(choices=LABEL_CHOICES, max_length=2)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    description = models.TextField()

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
    billing_address = models.ForeignKey('Address', related_name='billing_address',
                                        on_delete=models.SET_NULL, blank=True, null=True)
    shipping_address = models.ForeignKey('Address', related_name='shipping_address',
                                         on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', models.SET_NULL, blank=True, null=True)
    coupon = models.ForeignKey('Coupon', models.SET_NULL, blank=True, null=True)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
    reference_code = models.CharField(max_length=20)
    being_delivered = models.BooleanField(default=False)
    received = models.BooleanField(default=False)
    refund_requested = models.BooleanField(default=False)
    refund_granted = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

 

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    apartment_address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    address_type = models.CharField(max_length=1, choices=ADDRESS_CHOICES)
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

class Coupon(models.Model):
    coupon = models.CharField(max_length=30)
    amount = models.IntegerField()

    def __str__(self):
        return self.coupon

class Refund(models.Model):
    order = models.ForeignKey(Cart, on_delete=models.CASCADE)
    reference_code = models.CharField(max_length=20)
    reason = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return str(self.pk)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment

def user_profile_receiver(sender, instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Signal to create user profile every time a new user is created
post_save.connect(user_profile_receiver, sender=settings.AUTH_USER_MODEL)


class RawMaterial(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='items_images/')
    labels = models.CharField(choices=LABEL_CHOICES, max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.name

  

class BuildingSupply(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='items_images/')
    labels = models.CharField(choices=LABEL_CHOICES, max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class ConstructionEquipment(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='items_images/')
    labels = models.CharField(choices=LABEL_CHOICES, max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.name

   


class ArchitecturalProduct(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='items_images/')
    labels = models.CharField(choices=LABEL_CHOICES, max_length=2)
    description = models.TextField()

    def __str__(self):
        return self.name

   
