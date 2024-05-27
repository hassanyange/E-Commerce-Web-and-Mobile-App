from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="index" ),
    path('login/', views.signin, name='login'),
    path('userslist', views.userslist, name="userslist"),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('edit_user/<int:user_id>/', views.edit_user, name='edit_user'),
    path('materials', views.materiaslist, name="materialslist"),
    path('orders/', views.manage_orders, name='orders'),
    path('sales/', views.sales_overview, name='sales'),
    path('invoices/', views.invoice_list, name='invoices'),
    path('invoices/<int:id>/', views.invoice_detail, name='invoice_detail'),
    path('payments/', views.payment_list, name='payments'),
    path('payments/make/', views.make_payment, name='make_payment'),
]