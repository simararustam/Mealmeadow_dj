from django.http import JsonResponse
from ..models import Food

def get_food_detail(request, food_id):
    try:
        food = Food.objects.get(id=food_id)
        return JsonResponse(food.to_dict(), json_dumps_params={'indent': 2}, status=200)
    except Food.DoesNotExist:
        return JsonResponse({"message": "Yemek tapilmadi"}, status=404, json_dumps_params={'indent': 2})

def get_foods(request):
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('limit', 1))
    foods = Food.objects.all()[(page-1)*per_page:page*per_page]

    if not foods:
        return JsonResponse({"message": "Yemək tapılmadı"}, status=404)

    return JsonResponse({
        'foods': [f.to_dict() for f in foods],
        'total_food': Food.objects.count(),
        'page': page,
        'per_page': per_page
    }, status=200 , json_dumps_params={'indent': 2})

def get_all_foods(request):
    all_foods = Food.objects.all()
    food_data = [f.to_dict() for f in all_foods]
    return JsonResponse(food_data, safe=False, json_dumps_params={'indent': 2}, status = 200)