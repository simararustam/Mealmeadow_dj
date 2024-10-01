from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Restaurant
from ..serializers import RestaurantSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(
    method='get',
        manual_parameters=[
        openapi.Parameter('page', openapi.IN_QUERY, description="Page Number", type=openapi.TYPE_STRING),
        openapi.Parameter('limit', openapi.IN_QUERY, description="Number of Restaurant on per page", type=openapi.TYPE_STRING)
    ],
    responses={200: "Success"}
)
@api_view(['GET'])
def get_restaurants(request):
    '''sehifelemeye uygun deyerler qaytarir'''
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('limit', 8))
    restaurants = Restaurant.objects.all()[(page-1)*per_page:page*per_page]

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
)
@api_view(['POST'])
def create_restaurant(request):
    serializer = RestaurantSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, json_dums={'indent': 2})

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
    '''restoran id sine uygun detallari qaytarir'''
    try:
        restaurant = Restaurant.objects.get(pk=pk)
    except Restaurant.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = RestaurantSerializer(restaurant)
    return JsonResponse(serializer.data, json_dumps_params={'indent': 2}, safe=False)
