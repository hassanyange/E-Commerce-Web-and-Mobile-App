from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index" ),
    path('login/', views.signin, name='login'),
    path('userslist', views.userslist, name="userslist"),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('materials', views.materiaslist, name="materialslist")
]