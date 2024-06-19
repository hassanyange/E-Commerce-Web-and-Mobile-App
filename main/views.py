from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.db.models import Sum
from .forms import UserForm, CategoryForm, ItemForm, OrderStatusForm, LoginForm, CreateUserForm, OrderForm
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
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
        messages.error(request, 'Invalid username or password')
        return render(request, 'login.html', {'form': form})

def register(request):
    if request.method == 'GET':
        form = CreateUserForm()
        return render(request, 'register.html', {'form': form})
    elif request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User account successfully created')
            return redirect('login')
        else:
            return render(request, 'register.html', {'form': form})

def sign_out(request):
    logout(request)
    return redirect('login')

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def manage_orders(request):
    orders = Order.objects.all()
    return render(request, 'orders.html', {'orders': orders})

@login_required
def add_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('manage_orders')
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form': form})

@login_required
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

@login_required
def delete_order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('manage_orders')
    return render(request, 'delete_order.html', {'order': order})

@login_required
def sales_overview(request):
    sales = Item.objects.all()
    sales_data = []
    for item in sales:
        total_quantity = Order.objects.filter(items=item).count()
        total_sales = total_quantity * item.price
        sales_data.append({
            'item_name': item.item_name,
            'total_quantity': total_quantity,
            'total_sales': total_sales,
        })
    return render(request, 'sales.html', {'sales': sales_data})

@login_required
def invoice_list(request):
    invoices = Invoice.objects.filter(user=request.user)
    return render(request, 'invoices.html', {'invoices': invoices})

@login_required
def invoice_detail(request, id):
    invoice = get_object_or_404(Invoice, id=id, user=request.user)
    return render(request, 'invoice_detail.html', {'invoice': invoice})

@login_required
def payment_list(request):
    payments = Payment.objects.filter(user=request.user)
    return render(request, 'payments.html', {'payments': payments})

@login_required
def order_status(request, id):
    order = get_object_or_404(Order, id=id, user=request.user)
    return render(request, 'order_status.html', {'order': order})

@login_required
def userslist(request):
    customers = Customer.objects.all()
    return render(request, 'users-list.html', {'customers': customers})

@login_required
def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userslist')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

@login_required
def edit_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('userslist')
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})

@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('userslist')
    return render(request, 'delete_user.html', {'user': user})

@login_required
def item_list(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'item.html', {'items': items, 'categories': categories})

@login_required
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

@login_required
def edit_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    categories = Category.objects.all()  # Fetch all categories
    context = {
        'item': item,
        'categories': categories,
    }
    return render(request, 'edit_item.html', context)


@login_required
def delete_item(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'delete_item.html', {'item': item})

@login_required
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category.html', {'categories': categories})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

@login_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form': form})

@login_required
def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        category.delete()
        return redirect('category_list')
    return render(request, 'delete_category.html', {'category': category})

@login_required
def settings(request):
    return render(request, 'settings.html')

# New save views
@login_required
def add_user_save(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully added')
            return redirect('userslist')
    else:
        form = UserForm()
    return render(request, 'add_user.html', {'form': form})

@login_required
def add_order_save(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order successfully added')
            return redirect('manage_orders')
    else:
        form = OrderForm()
    return render(request, 'add_order.html', {'form': form})

@login_required
def add_category_save(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category successfully added')
            return redirect('category_list')
    else:
        form = CategoryForm()
    return render(request, 'add_category.html', {'form': form})

@login_required
def add_item_save(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item successfully added')
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

@login_required
def edit_user_save(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User successfully updated')
            return redirect('userslist')
    else:
        form = UserForm(instance=user)
    return render(request, 'edit_user.html', {'form': form, 'user': user})

@login_required
def edit_order_save(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            messages.success(request, 'Order successfully updated')
            return redirect('manage_orders')
    else:
        form = OrderForm(instance=order)
    return render(request, 'edit_order.html', {'form': form, 'order': order})

@login_required
def edit_item_save(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, 'Item successfully updated')
            return redirect('item_list')
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form, 'item': item})

@login_required
def edit_category_save(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            messages.success(request, 'Category successfully updated')
            return redirect('category_list')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form': form})
