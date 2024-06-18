from rest_framework import serializers
from main.models import User, Customer, Category, Item, Order, Address, Invoice, Payment, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'location', 'phone_number']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category']

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['item_name', 'category', 'price', 'item_image', 'description', 'seller_name']

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['user', 'street_address', 'postal_code', 'is_default']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'items', 'billing_address', 'shipping_address', 'payment', 'ordered_date', 'status', 'estimated_delivery_date', 'customer_name', 'product_name']

    def get_total(self, obj):
        total = sum([item.price for item in obj.items.all()])
        return total
