from rest_framework.views import APIView
from user.serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from utils.user_token import get_tokens_for_user

    
class UserRegistrationView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token = get_tokens_for_user(user)
        return Response(
            {'token': token, 'message': 'Registration Successful'},
            status=status.HTTP_201_CREATED
        )
