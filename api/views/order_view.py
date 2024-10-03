from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Restaurant, Food, Order, Notification
from ..serializers import OrderSerializer, NotificationSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='post', request_body=OrderSerializer)
@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        
        # Bildiriş yaratmaq
        Notification.objects.create(
            restaurant=order.restaurant,
            message=f"Yeni sifariş alindi: {order.id}, Məbləğ: {order.total_amount}."
        )
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_order(request, pk):
    # uygun id e gore order 
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = OrderSerializer(order)
    return JsonResponse(serializer.data, json_dumps_params={'indent': 2}, safe=False)

