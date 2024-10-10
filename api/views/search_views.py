from django.http import JsonResponse
from ..models.restaurant import Restaurant
from ..models.food import Food
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('query', openapi.IN_QUERY, description="Search query", type=openapi.TYPE_STRING),
        openapi.Parameter('food_type', openapi.IN_QUERY, description="Filter by food type (can be multiple)",
                          type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING)),
        openapi.Parameter('min_rating', openapi.IN_QUERY, description="Minimum rating filter",
                          type=openapi.TYPE_NUMBER),
        openapi.Parameter('max_rating', openapi.IN_QUERY, description="Maximum rating filter", type=openapi.TYPE_NUMBER)
    ],
    responses={200: "Success"}
)
@api_view(['GET'])
def search(request):
    query = request.GET.get('query', '')
    food_type = request.GET.getlist('food_type')
    min_rating = request.GET.get('min_rating', None)
    max_rating = request.GET.get('max_rating', None)

    restaurant_query = Restaurant.objects.filter(name__icontains=query)
    if min_rating:
        restaurant_query = restaurant_query.filter(rating__gte=min_rating)
    if max_rating:
        restaurant_query = restaurant_query.filter(rating__lte=max_rating)

    food_query = Food.objects.filter(name__icontains=query)
    if food_type:
        food_query = food_query.filter(food_type__in=food_type)

    restaurants = restaurant_query.all()
    foods = food_query.all()

    return JsonResponse({
        'restaurants': [r.to_dict() for r in restaurants],
        'foods': [f.to_dict() for f in foods],
    }, json_dumps_params={'indent': 2}, safe=False)


@swagger_auto_schema(
    method='get',
    manual_parameters=[
        openapi.Parameter('query', openapi.IN_QUERY, description="Search query", type=openapi.TYPE_STRING),
        openapi.Parameter('food_type', openapi.IN_QUERY, description="Filter by food type (can be multiple)",
                          type=openapi.TYPE_ARRAY, items=openapi.Items(type=openapi.TYPE_STRING)),
        openapi.Parameter('min_rating', openapi.IN_QUERY, description="Minimum rating filter",
                          type=openapi.TYPE_NUMBER),
        openapi.Parameter('max_rating', openapi.IN_QUERY, description="Maximum rating filter", type=openapi.TYPE_NUMBER)
    ],
    responses={200: "Success"}
)
@api_view(['GET'])
def search_all(request):
    query = request.GET.get('query', '')
    food_type = request.GET.getlist('food_type')
    min_rating = request.GET.get('min_rating', None)
    max_rating = request.GET.get('max_rating', None)

    restaurant_query = Restaurant.objects.all()
    if query:
        restaurant_query = restaurant_query.filter(name__icontains=query)
    if min_rating:
        restaurant_query = restaurant_query.filter(rating__gte=min_rating)
    if max_rating:
        restaurant_query = restaurant_query.filter(rating__lte=max_rating)

    food_query = Food.objects.all()
    if query:
        food_query = food_query.filter(name__icontains=query)
    if food_type:
        food_query = food_query.filter(food_type__in=food_type)

    restaurants = restaurant_query.all()
    foods = food_query.all()

    return JsonResponse({
        'restaurants': [r.to_dict() for r in restaurants],
        'foods': [f.to_dict() for f in foods],
    }, json_dumps_params={'indent': 2}, safe=False)