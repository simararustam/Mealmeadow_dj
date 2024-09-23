from django.http import JsonResponse
from ..models.restaurant import Restaurant
from ..models.food import Food

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
