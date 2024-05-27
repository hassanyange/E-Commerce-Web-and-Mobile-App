from django import forms
from .models import Customer, Category, Item, Payment

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'item_name', 'category', 'price', 'discount_price',
            'item_image', 'labels', 'slug', 'description'
        ]


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'email', 'location', 'picture', 'phone_number']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            'picture': forms.FileInput(attrs={'class': 'form-control-file'})
        }
