from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from ..models import Order

@api_view(['POST'])
@login_required
def send_receipt_email(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    
    # Email məzmunu
    subject = f"Order Receipt for Order {order.id}"
    message = f"Here is the receipt for your order from {order.restaurant.name}. Thank you for your purchase!"
    recipient = request.user.email
    
    # send_mail funksiyasını istifadə edərək email göndəririk
    send_mail(
        subject,
        message,
        'from@example.com',  # Göndərən email
        [recipient],         # Alıcı email
        fail_silently=False
    )
    
    return JsonResponse({'status': 'Receipt email sent successfully'}, status=200)
