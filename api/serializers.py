from rest_framework import serializers
from .models import Restaurant, Food, Order, Notification

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'restaurant', 'food_items']
        
class NotificationSerializer(serializers.ModelSerializer):
    class Meta():
        model = Notification
        fields = '__all__'

