from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index" ),
    path('userslist', views.userslist, name="userslist"),
    path('materials', views.materiaslist, name="materialslist")
]