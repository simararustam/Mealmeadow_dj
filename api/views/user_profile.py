from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from ..models import Profile, PaymentMethod, Address
from ..models.order import Order

@api_view(['GET'])
@login_required
def user_profile(request):
    profile = Profile.objects.get(user=request.user)
    payment_methods = PaymentMethod.objects.filter(user=request.user)
    addresses = Address.objects.filter(user=request.user)
    past_orders = Order.objects.filter(user=request.user, status__in=['Approved', 'Rejected'])

    profile_data = {
        'username': profile.user.username,
        'email': profile.user.email,
        'profile_image': profile.profile_image.url if profile.profile_image else None,
        'mobile_number': profile.mobile_number
    }

    payment_methods_data = [
        {
            'card_number': method.card_number,
            'expiration_date': method.expiration_date,
            'cardholder_name': method.cardholder_name
        }
        for method in payment_methods
    ]

    addresses_data = [
        {
            'address_type': address.address_type,
            'street_address': address.street_address,
            'city': address.city,
            'postal_code': address.postal_code
        }
        for address in addresses
    ]

    past_orders_data = [
        {
            'order_id': order.id,
            'restaurant_name': order.restaurant.name,
            'total_amount': sum([item.price for item in order.food_items.all()]),
            'order_date': order.order_date
        }
        for order in past_orders
    ]

    return JsonResponse({
        'profile': profile_data,
        'payment_methods': payment_methods_data,
        'addresses': addresses_data,
        'past_orders': past_orders_data
    }, safe=False)
