from django.urls import path
from .views.food_views import get_food_detail, get_foods, get_all_foods, submit_food
from .views.restaurant_views import get_restaurants, get_all_restaurants, get_restaurant_detail, edit_restaurant_profile
from .views.restaurant_views import create_restaurant
from .views.search_views import search, search_all
from .views.order_view import create_order, get_order
from .views.notifi_view import get_notifications
from .views.user_orders import user_orders
from .views.user_profile import user_profile 
from .views.edit_user_profile import edit_profile
from .views.send_receipt_email import send_receipt_email
from .views.login import RegisterView, LoginView

urlpatterns = [
    # Restaurant URLs
    path('restaurants/', get_restaurants, name='get_restaurants'),
    path('restaurants/all/', get_all_restaurants, name='get_all_restaurants'),
    path('restaurants/<int:pk>/', get_restaurant_detail, name='restaurant_detail'),
    path('restaurants/create/', create_restaurant, name='create_restaurant'),
    path('restaurants/<int:pk>/edit/', edit_restaurant_profile, name='edit_restaurant_profile'), 
    
    # Food URLs
    path('foods/<int:food_id>/', get_food_detail, name='food_detail'),
    path('foods/', get_foods, name='get_foods'),
    path('foods/all/', get_all_foods, name='get_all_foods'),
    path('foods/submit/', submit_food, name='submit_food'),
    
    #search URLs
    path('search/', search, name='search'), #hazir
    path('search/all/', search_all, name='search_all'), #hazir
    
    # Order URLs ??? create olmur
    path('orders/create/', create_order, name='create_order'),
    path('orders/<int:pk>/', get_order, name='get_order'),
    # !TEST
    path('user_orders/', user_orders, name='user_orders'),
    path('order/<int:order_id>/send-receipt/', send_receipt_email, name='send_receipt_email'),

    #??? Notification URLs
    path('restaurants/<int:restaurant_id>/notifications/', get_notifications, name='get_notifications'),

    #! user dashboard TEST
    path('user_profile/', user_profile, name='user_profile'),
    path('user_profile/edit/', edit_profile, name='edit_profile'),
    
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]

