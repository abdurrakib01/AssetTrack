from django.urls import path
from user.views import UserLoginView, UserRegistrationView


urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name="registration")
]