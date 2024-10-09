from django.http import JsonResponse
from ..models import Food, Restaurant
from rest_framework.decorators import api_view
from ..serializers import FoodSerializer
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@api_view(['GET'])
def get_food_detail(request, food_id):
    try:
        food = Food.objects.get(id=food_id)
        return JsonResponse(food.to_dict(), json_dumps_params={'indent': 2}, status=200)
    except Food.DoesNotExist:
        return JsonResponse({"message": "Yemek tapilmadi"}, status=404, json_dumps_params={'indent': 2})

@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('page', openapi.IN_QUERY, description="Page Number", type=openapi.TYPE_STRING),
        openapi.Parameter('limit', openapi.IN_QUERY, description="Number of food on per page", type=openapi.TYPE_STRING)
    ],
    responses={200: "Success"}
)
@api_view(['GET'])
def get_foods(request):
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('limit', 10))
    foods = Food.objects.all()[(page-1)*per_page:page*per_page]

    if not foods:
        return JsonResponse({"message": "Yemek tapilmadi"}, status=404)

    return JsonResponse({
        'foods': [f.to_dict() for f in foods],
        'total_food': Food.objects.count(),
        'page': page,
        'per_page': per_page
    }, status=200 , json_dumps_params={'indent': 2})

@api_view(['GET'])
def get_all_foods(request):
    all_foods = Food.objects.all()
    food_data = [f.to_dict() for f in all_foods]
    return JsonResponse(food_data, safe=False, json_dumps_params={'indent': 2}, status = 200)

# !-----partnyorlar-----
@swagger_auto_schema(method='post', request_body=FoodSerializer)
@api_view(['POST'])
def submit_food(request):
    serializer = FoodSerializer(data=request.data)
    if serializer.is_valid():
        if Food.objects.filter(name=serializer.validated_data['name']).exists():
            return Response({"error": "Bu yemek(qida) hazirda movcuddur"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put', request_body=FoodSerializer)
@api_view(['PUT'])
def edit_food(request, food_id):
    try:
        food_item = Food.objects.get(id=food_id)
    except Food.DoesNotExist:
        return Response({"error": "Yemek tapilmadi"}, status=status.HTTP_404_NOT_FOUND)

    restaurant_name = request.data.get('restaurant_name')

    if restaurant_name:
        try:
            restaurant = Restaurant.objects.get(name=restaurant_name)
            food_item.restaurant = restaurant
        except Restaurant.DoesNotExist:
            return Response({"error": "Restoran tapilmadi"}, status=status.HTTP_404_NOT_FOUND)

    serializer = FoodSerializer(food_item, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)