from ..models import Setting
from ..serializers import SettingSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['PUT'])
def update_settings(request, restaurant_id):
    try:
        setting = Setting.objects.get(restaurant_id=restaurant_id)
    except Setting.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    serializer = SettingSerializer(setting, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
