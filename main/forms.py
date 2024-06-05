from django import forms
from .models import Customer, Category, Item, Payment, Order

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



class CustomerForm(forms.ModelForm):
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