from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..models import Restaurant, Food, Order, Notification, OrderFood
from ..serializers import OrderSerializer, NotificationSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# @login_required
@swagger_auto_schema(method='post', request_body=OrderSerializer)
@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    
    if serializer.is_valid():
        order = serializer.save()

        user = order.user
        message = f"Yeni sifarish: {user.first_name} {user.last_name} ({user.email}):\n"
        message += "\n".join([f"{item.food.name} - {item.quantity}" for item in order.order_items.all()])

        Notification.objects.create(
            restaurant=order.restaurant,
            order=order,
            message=message,
            type='Order'
        )

        response_data = {
            "id": order.id,
            "user": order.user.id,
            "restaurant": order.restaurant.id,
            "order_items": [{"food_name": item.food.name, "quantity": item.quantity} for item in order.order_items.all()],
            "status": order.status,
            "order_date": order.order_date.isoformat(),
            "total_amount": str(order.total_amount)
        }

        return Response(response_data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_order(request, pk):
    try:
        order = Order.objects.get(pk=pk)
    except Order.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    response_data = {
        "id": order.id,
        "user": order.user.id,
        "restaurant": order.restaurant.id,
        "order_items": [{"food_name": item.food.name, "quantity": item.quantity} for item in order.order_items.all()],
        "status": order.status,
        "order_date": order.order_date.isoformat(),
        "total_amount": str(order.total_amount)
    }
    
    return Response(response_data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_all_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# !----------user_orders--------------
@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('user_id', openapi.IN_QUERY, description="User ID", type=openapi.TYPE_INTEGER),
        openapi.Parameter('page', openapi.IN_QUERY, description="Page Number", type=openapi.TYPE_INTEGER),
        openapi.Parameter('limit', openapi.IN_QUERY, description="Number of orders per page", type=openapi.TYPE_INTEGER)
    ],
    responses={200: OrderSerializer(many=True)}
)
@api_view(['GET'])
# @login_required
def get_orders_by_user(request):
    user_id = request.GET.get('user_id')
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 5))

    if not user_id:
        return Response({"message": "USER id tələb olunur"}, status=status.HTTP_400_BAD_REQUEST)

    orders = Order.objects.filter(user_id=user_id)
    
    if not orders.exists():
        return Response({"message": "Bu istifadəçi üçün heç bir sifariş tapılmadı"}, status=status.HTTP_404_NOT_FOUND)

    total_orders = orders.count()
    start_index = (page - 1) * limit
    end_index = start_index + limit
    paginated_orders = orders[start_index:end_index]

    serializer = OrderSerializer(paginated_orders, many=True)

    return Response({
        'orders': serializer.data,
        'total_orders': total_orders,
        'page': page,
        'limit': limit,
        'total_pages': (total_orders // limit) + (1 if total_orders % limit > 0 else 0)
    }, status=status.HTTP_200_OK)
