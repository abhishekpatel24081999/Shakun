from django.contrib.auth.models import User
from django.http import JsonResponse

def validate_username(request):
    email = request.GET.get('email', None)
    data = {
        'is_taken': User.objects.filter(email__iexact=email).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this email already exists.'

    print(data['is_taken'])
    return JsonResponse(data)