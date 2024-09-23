from django.urls import path
from .views.food_views import get_food_detail, get_foods, get_all_foods
from .views.restaurant_views import get_restaurants, get_all_restaurants
from .views.search_views import search, search_all

urlpatterns = [
    path('foods/<int:food_id>/', get_food_detail, name='food_detail'), #hazir
    path('foods/', get_foods, name='get_foods'), #hazir
    path('foods/all/', get_all_foods, name='get_all_foods'), #hazir
    path('restaurants/', get_restaurants, name='get_restaurants'), #hazir
    path('restaurants/all/', get_all_restaurants, name='get_all_restaurants'), #hazir
    path('search/', search, name='search'), #hazir
    path('search/all/', search_all, name='search_all'), #hazir
]
