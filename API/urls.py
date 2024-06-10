from django.urls import path
from .views import (
    RegistrationViewSet,
    CustomerViewSet,
    CategoryViewSet,
    ItemViewSet,
    OrderItemViewSet,
    CartViewSet,
    OrderViewSet,
    AddressViewSet,
    InvoiceViewSet,
    PaymentViewSet,
    CommentViewSet,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    # User Authentication
    path('users/create/', RegistrationViewSet.as_view({'post': 'register'}), name='create_user'),
    path('users/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Resources
    path('customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'}), name='customer_list'),
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category_list'),
    path('items/', ItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='item_list'),
    path('orderitems/', OrderItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='orderitem_list'),
    path('carts/', CartViewSet.as_view({'get': 'list', 'post': 'create'}), name='cart_list'),
    path('orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order_list'),
    path('addresses/', AddressViewSet.as_view({'get': 'list', 'post': 'create'}), name='address_list'),
    path('invoices/', InvoiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='invoice_list'),
    path('payments/', PaymentViewSet.as_view({'get': 'list', 'post': 'create'}), name='payment_list'),
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment_list'),

    # Individual Resource and Actions
    path('customers/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='customer_detail'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category_detail'),
    path('items/<int:pk>/', ItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='item_detail'),
    path('orderitems/<int:pk>/', OrderItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='orderitem_detail'),
    path('carts/<int:pk>/', CartViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='cart_detail'),
    path('orders/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='order_detail'),
    path('addresses/<int:pk>/', AddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='address_detail'),
    path('invoices/<int:pk>/', InvoiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='invoice_detail'),
    path('payments/<int:pk>/', PaymentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='payment_detail'),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment_detail'),
]
