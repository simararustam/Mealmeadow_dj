from ..models import Order
from ..serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import JsonResponse

@api_view(['POST'])
def create_order(request):
    # yeni sifaris yaradir
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
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
    # return JsonResponse(serializer.data, json_dumps={'indent': 2})
    return Response(serializer.data)
