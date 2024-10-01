from django.urls import path, re_path
from .views.food_views import get_food_detail, get_foods, get_all_foods, submit_food_for_approval
from .views.restaurant_views import get_restaurants, get_all_restaurants, get_restaurant_detail, edit_restaurant_profile
from api.views.restaurant_views import create_restaurant
from .views.search_views import search, search_all
from .views.order_view import create_order, get_order
from .views.notifi_view import get_notifications
from .views.setting_view import update_settings


urlpatterns = [
    # Restaurant URLs
    path('restaurants/', get_restaurants, name='get_restaurants'), #OK
    path('restaurants/all/', get_all_restaurants, name='get_all_restaurants'), #OK
    path('restaurants/<int:pk>/', get_restaurant_detail, name='restaurant_detail'), #OK
    
    path('restaurants/create/', create_restaurant, name='create_restaurant'),#OK
    path('restaurants/<int:pk>/edit/', edit_restaurant_profile, name='edit_restaurant_profile'), #OK
    
    # Food URLs
    path('foods/<int:food_id>/', get_food_detail, name='food_detail'), #OK
    path('foods/', get_foods, name='get_foods'),#OK pagination
    path('foods/all/', get_all_foods, name='get_all_foods'),#ok
    path('foods/submit/', submit_food_for_approval, name='submit_food_for_approval'),#OK
    
    #search URLs
    path('search/', search, name='search'), #hazir
    path('search/all/', search_all, name='search_all'), #hazir
    
    # Order URLs
    path('orders/', create_order, name='create_order'), #hazir
    path('orders/<int:pk>/', get_order, name='get_order'), #hazir ama baxacam

    # Notification URLs
    path('restaurants/<int:restaurant_id>/notifications/', get_notifications, name='get_notifications'), #deqiqlesdirecem

    # Settings URLs
    path('restaurants/<int:restaurant_id>/settings/', update_settings, name='update_settings'), #deqiqlesdirmek lazimdi

]

