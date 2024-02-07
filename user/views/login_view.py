from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from user.serializers import LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate
from utils.user_token import get_tokens_for_user


class UserLoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.validated_data)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            token = get_tokens_for_user(user)
            return Response({'token':token, 'msg':'Login Successful'}, status=status.HTTP_200_OK)
        return Response(
            {'non_field_errors':['email or password is not valid']},
            status=status.HTTP_404_NOT_FOUND
        )