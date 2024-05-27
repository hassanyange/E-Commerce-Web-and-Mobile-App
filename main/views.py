from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from .forms import CustomerForm

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