from ..models import Notification
from ..serializers import NotificationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

@api_view(['GET'])
def get_notifications(request, restaurant_id):
    # restorana uygunb bildiris qaytarir ama buna baxacam
    notifications = Notification.objects.filter(restaurant_id=restaurant_id)
    serializer = NotificationSerializer(notifications, many=True)
    return Response(serializer.data)
