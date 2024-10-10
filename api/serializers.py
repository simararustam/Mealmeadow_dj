from rest_framework import serializers
from .models import Address, Restaurant, Food, Order, Notification, OrderFood, PaymentMethod
from django.contrib.auth import get_user_model


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class FoodSerializer(serializers.ModelSerializer):
    restaurant_name = serializers.CharField(source='restaurant.name', read_only=True)

    class Meta:
        model = Food
        fields = ['id', 'name', 'food_type', 'price',
                  'discounted_price', 'discounted_rate',
                  'description', 'restaurant_name',
                  'restaurant', 'quantity', 'elan_muddeti', 'mehsul_muddeti', 'image']


class NotificationSerializer(serializers.ModelSerializer):
    class Meta():
        model = Notification
        fields = '__all__'


class OrderFoodSerializer(serializers.ModelSerializer):
    food_name = serializers.CharField(source='food.name', read_only=True)

    class Meta:
        model = OrderFood
        fields = ['food', 'food_name', 'quantity']


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderFoodSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'restaurant', 'order_items', 'status', 'order_date', 'total_amount']
        read_only_fields = ['id', 'order_date', 'total_amount']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        order = Order.objects.create(**validated_data)

        for item_data in order_items_data:
            OrderFood.objects.create(order=order, **item_data)

        order.calculate_total_amount()

        return order


# !---------USER profile------------------------
User = get_user_model()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'last_name', 'phone', 'email', 'image', 'birth_date', 'gender']