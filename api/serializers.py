from rest_framework import serializers
from .models import Restaurant, Food, Order, Notification, Setting

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    food_items = FoodSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Setting
        fields = '__all__'
