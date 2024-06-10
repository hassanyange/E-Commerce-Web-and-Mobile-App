from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name="index" ),
    path('', views.signin, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.sign_out, name='logout'),
    path('userslist', views.userslist, name="userslist"),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('items/', views.item_list, name='item_list'),
    path('items/add/', views.add_item, name='add_item'),
    path('orders/', views.manage_orders, name='orders'),
    path('order/<int:id>/', views.order_status, name='order_status'),
    path('sales/', views.sales_overview, name='sales'),
    path('invoices/', views.invoice_list, name='invoices'),
    path('invoices/<int:id>/', views.invoice_detail, name='invoice_detail'),
    path('payments/', views.payment_list, name='payments'),
    path('settings', views.settings, name='settings',)
]