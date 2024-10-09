from django.urls import path
from .views.food_views import get_food_detail, get_foods, get_all_foods, submit_food, edit_food
from .views.restaurant_views import get_restaurants, get_all_restaurants, get_restaurant_detail, edit_restaurant_profile, get_foods_by_restaurant
from .views.restaurant_views import create_restaurant
from .views.search_views import search, search_all
from .views.order_view import create_order, get_order, get_orders_by_user, get_all_orders
from .views.notifi_view import get_notifications
from .views.user_profile import user_profile, all_users
from .views.edit_user_profile import edit_profile
from .views.send_receipt_email import send_receipt_email

urlpatterns = [
    # Restaurant URLs
    path('restaurants/', get_restaurants, name='get_restaurants'),
    path('restaurants/all/', get_all_restaurants, name='get_all_restaurants'),
    path('restaurants/<int:pk>/', get_restaurant_detail, name='restaurant_detail'),
    path('restaurants/create/', create_restaurant, name='create_restaurant'),
    path('restaurants/<int:pk>/edit/', edit_restaurant_profile, name='edit_restaurant_profile'), 
    path('restaurants/<int:restaurant_id>/notifications/', get_notifications, name='get_notifications'),
    path('restaurants/<int:restaurant_id>/foods/', get_foods_by_restaurant, name='get_foods_by_restaurant'),

    # Food URLs
    path('food/<int:food_id>/', get_food_detail, name='food_detail'),
    path('food/', get_foods, name='get_foods'),
    path('food/all/', get_all_foods, name='get_all_foods'),
    path('food/submit/', submit_food, name='submit_food'),
    path('food/edit/<int:food_id>/', edit_food, name='edit_food'),
    
    #search URLs
    path('search/', search, name='search'), #hazir
    path('search/all/', search_all, name='search_all'), #hazir
    
    # Order URLs
    path('order/create/', create_order, name='create_order'),
    path('order/<int:pk>/', get_order, name='get_order'),
    path('order/all/', get_all_orders, name='get_order'),
    path('user_orders/', get_orders_by_user, name='user_orders'),
    path('order/<int:order_id>/send-receipt/', send_receipt_email, name='send_receipt_email'),

    # User Urls
    path('user/edit/<int:user_id>/', edit_profile, name='edit_profile'),
    path('user/<int:user_id>/', user_profile, name='user_profile'),
    path('users/', all_users, name='all_users'),
]
