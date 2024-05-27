from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import CustomerForm, CategoryForm, ItemForm, PaymentForm
from .models import *



def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('index')  # Use the name defined in the URL pattern
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')  # Use the name defined in the URL pattern

    return render(request, 'login.html')



@login_required
def index(request):
    return render(request, 'index.html')


def add_customer(request):
    if request.method == 'GET':
        form = CustomerForm()
        return render(request, 'users-list.html', {'form': form})
    elif request.method == 'POST':
        form = CustomerForm()
        if form.is_valid():
            form.save()
            # Redirect to a success page or any other view after adding the customer
            return redirect('userlist')  
    else:
        form = CustomerForm()
    return render(request, 'users-list.html', {'form': form})

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




@login_required
def manage_orders(request):
    orders = Cart.objects.filter(ordered=True)
    context = {'orders': orders}
    return render(request, 'orders.html', context)

@login_required
def sales_overview(request):
    # Assuming you want to aggregate sales data
    sales = Item.objects.all()  # Customize this query based on your sales logic
    sales_data = []
    for item in sales:
        total_quantity = OrderItem.objects.filter(item=item).aggregate(total_quantity=Sum('quantity'))['total_quantity'] or 0
        total_sales = total_quantity * item.price
        sales_data.append({
            'item_name': item.item_name,
            'total_quantity': total_quantity,
            'total_sales': total_sales,
        })
    context = {'sales': sales_data}
    return render(request, 'sales.html', context)




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
def make_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.user = request.user
            payment.successful = True  # This would normally be set by your payment gateway
            payment.save()
            return redirect('dashboard:payments')
    else:
        form = PaymentForm()
    return render(request, 'make_payment.html', {'form': form})


def userslist(request):
    return render(request,'users-list.html')

def materiaslist(request):
    return render(request, 'materials.html')