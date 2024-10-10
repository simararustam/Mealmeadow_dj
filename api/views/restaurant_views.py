from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from services.to_distance import calculate_distance
from ..models import Restaurant, Food
from ..serializers import RestaurantSerializer, FoodSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('page', openapi.IN_QUERY, description="Page Number", type=openapi.TYPE_STRING),
        openapi.Parameter('limit', openapi.IN_QUERY, description="Number of Restaurant on per page",
                          type=openapi.TYPE_STRING)
    ],
    responses={200: "Success"}
)
@api_view(['GET'])
def get_restaurants(request):
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('limit', 5))
    restaurants = Restaurant.objects.all()[(page - 1) * per_page:page * per_page]

    return JsonResponse({
        'restaurants': [r.to_dict() for r in restaurants],
        'total_restaurant': Restaurant.objects.count(),
        'page': page,
        'per_page': per_page
    }, json_dumps_params={'indent': 2}, status=200)


@api_view(['GET'])
def get_all_restaurants(request):
    '''butun restoranlari qaytarir'''
    all_restaurants = Restaurant.objects.all()
    rest_data = [r.to_dict() for r in all_restaurants]
    return JsonResponse(rest_data, json_dumps_params={'indent': 2}, safe=False)


# !----Partnyorlar dashbordu üçün--------

@swagger_auto_schema(
    method='post',
    request_body=RestaurantSerializer,
    consumes=['multipart/form-data']
)
@api_view(['POST'])
def create_restaurant(request):
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method='put',
    request_body=RestaurantSerializer,
)
@api_view(['PUT'])
def edit_restaurant_profile(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RestaurantSerializer(restaurant, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_restaurant_detail(request, pk):
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = RestaurantSerializer(restaurant)
    return JsonResponse(serializer.data, json_dumps_params={'indent': 2}, safe=False)


# !---------------------
@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('restaurant_id', openapi.IN_PATH, description="ID of the restaurant",
                          type=openapi.TYPE_INTEGER),
    ],
    responses={200: FoodSerializer(many=True)},
    operation_description="Retrieve all food items for a specific restaurant."
)
@api_view(['GET'])
def get_foods_by_restaurant(request, restaurant_id):
    try:
        restaurant = Restaurant.objects.get(id=restaurant_id)
        foods = Food.objects.filter(restaurant=restaurant)
        serializer = FoodSerializer(foods, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Restaurant.DoesNotExist:
        return Response({'error': 'Restoran Tapılmadı'}, status=status.HTTP_404_NOT_FOUND)

"""
Nearby
"""

@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('lat', openapi.IN_QUERY, description="User Latitude", type=openapi.TYPE_STRING),
        openapi.Parameter('lon', openapi.IN_QUERY, description="User Longitude", type=openapi.TYPE_STRING),
        openapi.Parameter('page', openapi.IN_QUERY, description="Page Number", type=openapi.TYPE_STRING),
        openapi.Parameter('limit', openapi.IN_QUERY, description="Number of Restaurants per Page",
                          type=openapi.TYPE_STRING)
    ],
    responses={200: "Success"}
)
@api_view(['GET'])
def get_nearby_restaurants(request):
    '''User-in 1km yakinligindaki restoranlari qaytarir'''

    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    # Check if lat and lon are provided
    if not lat or not lon:
        return Response({'error': 'Latitude and Longitude are required'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        user_lat = float(lat)
        user_lon = float(lon)
    except ValueError:
        return Response({'error': 'Invalid latitude or longitude format'}, status=status.HTTP_400_BAD_REQUEST)

    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('limit', 5))

    # Find restaurants within 1 km
    nearby_restaurants = []
    for restaurant in Restaurant.objects.all():
        distance = calculate_distance(user_lat, user_lon, restaurant.latitude, restaurant.longitude)
        if distance <= 1000:  # 1 km radius
            restaurant_data = restaurant.to_dict()
            restaurant_data['distance'] = round(distance, 2)  # Include the distance in the response
            nearby_restaurants.append(restaurant_data)

    # Paginate the results
    start = (page - 1) * per_page
    end = start + per_page
    paginated_restaurants = nearby_restaurants[start:end]

    return JsonResponse({
        'restaurants': paginated_restaurants,
        'total_restaurants': len(nearby_restaurants),
        'page': page,
        'per_page': per_page
    }, json_dumps_params={'indent': 2}, status=200)