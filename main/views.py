from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

@login_required
def index(request):
    return render(request, 'index.html')



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