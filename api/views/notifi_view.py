from ..models import Notification
from ..serializers import NotificationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(method='get', responses={200: NotificationSerializer(many=True)})
@api_view(['GET'])
def get_notifications(request, restaurant_id):
    notifications = Notification.objects.filter(restaurant_id=restaurant_id)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)
