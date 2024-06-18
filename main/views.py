from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.db.models import Sum
from .forms import UserForm, CategoryForm, ItemForm, OrderStatusForm,LoginForm,CreateUserForm
from .forms import OrderForm
from .models import *



def signin(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', {'form': form})
    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                # messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('index')
        
        # form is not valid or user is not authenticated
        messages.error(request,f'Invalid username or password')
        return render(request,'login.html',{'form': form})
 
    
def register(request):
    if request.method == 'GET':
        form = CreateUserForm()
        return render(request, 'register.html', { 'form': form})
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'user account succesful created')
            return redirect('login')
            
        else: 
            context = {'form':form}
            return render(request, 'register.html', context)



def sign_out(request):
    logout(request)
    # messages.success(request,f'You have been logged out.')
    return redirect('login') 


# @login_required
def index(request):
    return render(request, 'index.html')



#   ORDERS

# @login_required
def manage_orders(request):
    orders = Order.objects.all()
    context = {
        'orders': orders
    }
    return render(request, 'orders.html', context)



def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_orders')
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form': form})

def edit_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('manage_orders')
    else:
        form = OrderForm(instance=order)
    return render(request, 'edit_order.html', {'form': form, 'order': order})

def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('manage_orders')
    return render(request, 'delete_order.html', {'order': order})

# @login_required
def sales_overview(request):
    # Assuming you want to aggregate sales data
    sales = Item.objects.all()  # Customize this query based on your sales logic
    sales_data = []
    for item in sales:
        # Use Django's Sum function to aggregate quantity
        total_quantity = Order.objects.filter(item=item).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        total_sales = total_quantity * item.price
        sales_data.append({
            'item_name': item.item_name,
            'total_quantity': total_quantity,
            'total_sales': total_sales,
        })
    context = {'sales': sales_data}
    return render(request, 'sales.html', context)


# @login_required
def invoice_list(request):
    invoices = Invoice.objects.filter(user=request.user)
    return render(request, 'invoices.html', {'invoices': invoices})

# @login_required
def invoice_detail(request, id):
    invoice = get_object_or_404(Invoice, id=id, user=request.user)
    return render(request, 'invoice_detail.html', {'invoice': invoice})

# @login_required
def payment_list(request):
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'payments.html', {'payments': payments})


def order_status(request, id):
    order = get_object_or_404(Order, id=id, user=request.user )
    return render(request, 'order_status.html', {'order': order})

#    USER LIST
def userslist(request):
    customers = Customer.objects.all()
    return render(request, 'users-list.html', {'customers': customers})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users_list')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users_list')
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})

def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('users_list')
    return render(request, 'delete_user.html', {'user': user})




                                 #   ITEMS
def item_list(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'item.html', {'items': items, 'categories': categories})

def add_item(request):
    categories = Category.objects.all()
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form, 'categories': categories})


def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form, 'item': item})

        # CATEGORY
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form': form})

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'delete_category.html', {'category': category})





def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'delete_item.html', {'item': item})



def settings(request):
    return render(request, 'settings.html')