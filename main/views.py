from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def userslist(request):
    return render(request,'users-list.html')