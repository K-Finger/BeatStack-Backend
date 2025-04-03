from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from users.serializers import UserRegistrationSerializer

@api_view(['POST'])
def registration_view (request):
    serializer = UserRegistrationSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        user = serializer.save()
        data['response'] = 'successfully registered new user.'
        data['email'] = user.email
    else:
        data = serializer.errors
    return Response(data)