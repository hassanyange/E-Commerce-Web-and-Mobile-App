from django.urls import path
from .views import (
    RegistrationViewSet,
    CustomerViewSet,
    CategoryViewSet,
    ItemViewSet,
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
    path('customers/', CustomerViewSet.as_view({'get': 'list', 'post': 'create'}), name='customer-list'),
    path('categories/', CategoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='category-list'),
    path('items/', ItemViewSet.as_view({'get': 'list', 'post': 'create'}), name='item-list'),
    path('orders/', OrderViewSet.as_view({'get': 'list', 'post': 'create'}), name='order-list'),
    path('addresses/', AddressViewSet.as_view({'get': 'list', 'post': 'create'}), name='address-list'),
    path('invoices/', InvoiceViewSet.as_view({'get': 'list', 'post': 'create'}), name='invoice-list'),
    path('payments/', PaymentViewSet.as_view({'get': 'list', 'post': 'create'}), name='payment-list'),
    path('comments/', CommentViewSet.as_view({'get': 'list', 'post': 'create'}), name='comment-list'),

    # Individual Resource and Actions
    path('customers/<int:pk>/', CustomerViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='customer-detail'),
    path('categories/<int:pk>/', CategoryViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='category-detail'),
    path('items/<int:pk>/', ItemViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='item-detail'),
    path('orders/<int:pk>/', OrderViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='order-detail'),
    path('addresses/<int:pk>/', AddressViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='address-detail'),
    path('invoices/<int:pk>/', InvoiceViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='invoice-detail'),
    path('payments/<int:pk>/', PaymentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='payment-detail'),
    path('comments/<int:pk>/', CommentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='comment-detail'),
]
