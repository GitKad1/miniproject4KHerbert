
from django.urls import path
from .views import register, user_login, order_index, order_pizza, user_logout, place_order


urlpatterns = [
    path('register/', register, name='register'),
    path('orderIndex/', order_index, name='orderIndex'),
    path('orderPizza/', order_pizza, name='orderPizza'),
    path('place-order/', place_order, name='place_order'),
    path('', order_index, name='orderIndex'),
    path('logout', user_logout, name='logout'),
    path('accounts/login/', user_login, name='login'),
    # Add other URL patterns as needed
]

