from rest_framework.views import APIView
from user.serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, authenticate
from utils.user_token import get_tokens_for_user


class UserLoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            token = get_tokens_for_user(user)
            return Response({'token': token, 'message': 'Login Successful'}, status=status.HTTP_200_OK)
        return Response(
            {'detail': 'email or password is not valid'},
            status=status.HTTP_404_NOT_FOUND
        )
