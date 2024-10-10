from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status
from ..serializers import UserProfileSerializer

User = get_user_model()

# ! COMMENTDƏN ÇIXART
@swagger_auto_schema(
     method='put', 
     request_body=UserProfileSerializer,
)
@api_view(['PUT'])
def edit_profile(request, user_id):
    try:
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({'error': 'İstifadəçi Tapılmadı'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserProfileSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

