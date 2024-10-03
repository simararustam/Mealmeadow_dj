from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from ..models import Profile

@csrf_exempt
@api_view(['POST'])
@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)

    profile.mobile_number = request.data.get('mobile_number')
    if request.FILES.get('profile_image'):
        profile.profile_image = request.FILES.get('profile_image')
    profile.save()
    
    return JsonResponse({'status': 'Profile updated successfully'}, status=200)
