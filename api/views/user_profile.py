from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

User = get_user_model()


@api_view(['GET'])
def user_profile(request, user_id):
    try:
        user = User.objects.get(id=user_id)

        user_data = {
            'name': user.name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
            'image': user.image.url if user.image else None,
            'birth_date': user.birth_date,
            'gender': user.gender,
            'created_at': user.created_at,
            'updated_at': user.updated_at,
        }
        return Response(user_data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'error': 'İstifadəçi Tapılmadı'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_users(request):
    users = User.objects.all()

    users_data = []
    for user in users:
        users_data.append({
            'name': user.name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.phone,
            'image': user.image.url if user.image else None,
            'birth_date': user.birth_date,
            'gender': user.gender,
            'created_at': user.created_at,
            'updated_at': user.updated_at,
        })
    return Response(users_data, status=status.HTTP_200_OK)