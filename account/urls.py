from django.urls import path, include


from account.views import UserRegistrationGenericAPIView

urlpatterns = [
    path('users/', UserRegistrationGenericAPIView.as_view()),
    path('user/<int:pk>/', UserRegistrationGenericAPIView.as_view()),
]