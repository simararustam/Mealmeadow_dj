from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from ..models import Order
from ..serializers import OrderSerializer
from django.conf import settings
from rest_framework.permissions import IsAuthenticated

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def send_receipt_email(request, order_id):
    '''
    Authentifikasiya problemi var 
    '''
    order = get_object_or_404(Order, id=order_id, user=request.user)
    
    serializer = OrderSerializer(order)

    subject = f"Sifariş çeki #{order.id}"
    message = f"Sifariş Detalları:\n\nRestoran: {order.restaurant.name}\nSifariş Tarixi: {order.order_date.strftime('%Y-%m-%d %H:%M:%S')}\n\nYeməklər:\n"

    for item in serializer.data['order_items']:
        message += f"- {item['food_name']}: {item['quantity']} ədəd\n"

    message += f"\nÜmumi məbləğ: {serializer.data['total_amount']} AZN"

    recipient = request.user.email
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [recipient],
        fail_silently=False
    )

    return JsonResponse({'status': 'Çek uğurla göndərildi'}, status=status.HTTP_200_OK)
