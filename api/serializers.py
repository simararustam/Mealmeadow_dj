from rest_framework import serializers
from .models import Restaurant, Food, Order, Notification, Setting

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta():
        model = Restaurant
        fields = ['name', 'category', 'rating', 'owner_name', 'contact_number', 'email', 'logo']

class FoodSerializer(serializers.ModelSerializer):
    class Meta():
        model = Food
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['user', 'restaurant', 'food_items']

class NotificationSerializer(serializers.ModelSerializer):
    class Meta():
        model = Notification
        fields = '__all__'

class SettingSerializer(serializers.ModelSerializer):
    class Meta():
        model = Setting
        fields = '__all__'
