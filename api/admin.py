from django.contrib import admin
from api.models import (Address, Food, OrderFood,
                        Notification, Order, PaymentMethod,
                        Profile, Rating, Restaurant)


admin.site.register(Address)
admin.site.register(Food)
admin.site.register(OrderFood)
admin.site.register(PaymentMethod)
admin.site.register(Notification)
admin.site.register(Order)
admin.site.register(Restaurant)
admin.site.register(Rating)
admin.site.register(Profile)

