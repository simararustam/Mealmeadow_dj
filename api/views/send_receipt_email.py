from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from ..models import Order

@api_view(['POST'])
@login_required
def send_receipt_email(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)

    subject = f"Sifariş çeki {order.id}"
    message = f"{order.restaurant.name}"
    recipient = request.user.email
    
    send_mail(
        subject,
        message,
        'from@example.com',
        [recipient],
        fail_silently=False
    )
    
    return JsonResponse({'status': 'Çek uğurla göndərildi'}, status=200)
