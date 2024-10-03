from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ..models import Order
# !USER DASHBORAD

@api_view(['GET'])
@login_required
def order_detail(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)

    order_data = {
        'order_id': order.id,
        'restaurant_name': order.restaurant.name,
        'status': order.status,
        'order_date': order.order_date,
        'food_items': [
            {
                'food_name': item.name,
                'price': item.price,
                'discounted_price': item.discounted_price
            }
            for item in order.food_items.all()
        ]
    }

    return JsonResponse(order_data, safe=False)
