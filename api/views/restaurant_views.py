from django.http import JsonResponse
from ..models.restaurant import Restaurant

def get_restaurants(request):
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('limit', 8))
    restaurants = Restaurant.objects.all()[(page-1)*per_page:page*per_page]

    return JsonResponse({
        'restaurants': [r.to_dict() for r in restaurants],
        'total_restaurant': Restaurant.objects.count(),
        'page': page,
        'per_page': per_page
    }, json_dumps_params={'indent': 2}, status=200)

def get_all_restaurants(request):
    all_restaurants = Restaurant.objects.all()
    rest_data = [r.to_dict() for r in all_restaurants]
    return JsonResponse(rest_data, json_dumps_params={'indent': 2}, safe=False)
