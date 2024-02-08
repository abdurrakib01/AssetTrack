from django.urls import path
from user.views import UserLoginView, UserRegistrationView


urlpatterns = [
    path('user/login/', UserLoginView.as_view(), name='login'),
    path('user/registration/', UserRegistrationView.as_view(), name="registration")
]
