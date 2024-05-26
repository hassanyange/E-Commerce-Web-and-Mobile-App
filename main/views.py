from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import CustomerForm

@login_required
def index(request):
    return render(request, 'index.html')


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Redirect to a success page or any other view after adding the customer
            return redirect('userlist')  
    else:
        form = CustomerForm()
    return render(request, 'users-list.html', {'form': form})

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

def userslist(request):
    return render(request,'users-list.html')

def materiaslist(request):
    return render(request, 'materials.html')