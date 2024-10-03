from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ..models import Order

@api_view(['GET'])
@login_required
def user_orders(request):
    # Cari sifarişlər (yalnız ilk 5 sifariş)
    current_orders = Order.objects.filter(user=request.user, status='Pending')[:5]
    # Tarixçə sifarişləri (6+ sifariş)
    past_orders = Order.objects.filter(user=request.user, status__in=['Approved', 'Rejected'])[5:]

    current_orders_data = [
        {
            'order_id': order.id,
            'restaurant_name': order.restaurant.name,
            'status': order.status,
            'order_date': order.order_date
        }
        for order in current_orders
    ]
    
    past_orders_data = [
        {
            'order_id': order.id,
            'restaurant_name': order.restaurant.name,
            'status': order.status,
            'order_date': order.order_date
        }
        for order in past_orders
    ]

    return JsonResponse({
        'current_orders': current_orders_data,
        'past_orders': past_orders_data
    }, safe=False)
