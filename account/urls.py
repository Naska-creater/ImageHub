from django.urls import path, include


from account.views import UserRegistrationGenericAPIView, UsersGenericAPIView

urlpatterns = [
    path('user/registration/', UserRegistrationGenericAPIView.as_view()),
    path('users/', UsersGenericAPIView.as_view()),
]