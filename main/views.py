from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages
from django.db.models import Sum
from .forms import CustomerForm, CategoryForm, ItemForm, OrderStatusForm,LoginForm,CreateUserForm
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


def add_customer(request):
    if request.method == 'GET':
        form = CustomerForm()
        return render(request, 'add_customer.html', {'form': form})
    elif request.method == 'POST':
        form = CustomerForm()
        if form.is_valid():
            form.save()
            # Redirect to a success page or any other view after adding the customer
            return redirect('userlist')  
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})



def edit_user(request, user_id):
    # Get the user object from the database
    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        # Populate the form with the user's data from the request
        form = CustomerForm(request.POST, instance=user)
        if form.is_valid():
            # Save the updated user information
            form.save()
            # Redirect to the user list page or any other page as needed
            return redirect('userlist')
    else:
        # Populate the form with the user's current data
        form = CustomerForm(instance=user)




# @login_required
def manage_orders(request):
    orders = Cart.objects.filter(ordered=True)
    context = {'orders': orders}
    return render(request, 'orders.html', context)

# @login_required
def sales_overview(request):
    # Assuming you want to aggregate sales data
    sales = Item.objects.all()  # Customize this query based on your sales logic
    sales_data = []
    for item in sales:
        # Use Django's Sum function to aggregate quantity
        total_quantity = OrderItem.objects.filter(item=item).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
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


def userslist(request):
    # Retrieve all customers from the database
    customers = Customer.objects.all()
    return render(request, 'users-list.html', {'customers': customers})


def item_list(request):
    items = Item.objects.all()
    categories = Category.objects.all()
    return render(request, 'item.html', {'items': items, 'categories': categories})

def add_item(request):
    if request.method == 'POST':
        item_name = request.POST['item_name']
        category_id = request.POST['category']
        price = request.POST['price']
        description = request.POST['description']
        seller_name = request.POST['seller_name']
        item_image = request.FILES['item_image']

        category = Category.objects.get(id=category_id)
        new_item = Item(item_name=item_name, category=category, price=price, description=description, seller_name=seller_name, item_image=item_image)
        new_item.save()
        return redirect('item_list')
    else:
        categories = Category.objects.all()
        return render(request, 'addItem.html', {'categories': categories})



def settings(request):
    return render(request, 'settings.html')