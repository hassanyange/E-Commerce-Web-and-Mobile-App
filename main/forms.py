from django import forms
from .models import Customer, Category, Item, Payment, Order
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'item_name', 'category', 'price', 
            'item_image',   'description', 'seller_name'
        ]

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)

class CreateUserForm(UserCreationForm):
   

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['username', 'email', 'location', 'phone_number']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OrderStatusForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'estimated_delivery_date']


from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'product_name', 'billing_address', 'shipping_address', 'payment', 'estimated_delivery_date', 'status']



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'category', 'price', 'item_image', 'description', 'seller_name']
        widgets = {
            'item_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter item name'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter price'}),
            'item_image': forms.FileInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Enter description'}),
            'seller_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter seller name'}),
        }