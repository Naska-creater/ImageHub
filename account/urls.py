from django.urls import path, include


from account.views import UserRegistrationGenericAPIView, UserChangeGenericAPIView, AdminChangeGenericAPIView

urlpatterns = [
    path('user/registration/', UserRegistrationGenericAPIView.as_view()),
    path('user/change/', UserChangeGenericAPIView.as_view()),
    path('admin/change/<int:pk>/', AdminChangeGenericAPIView.as_view()),
    path('admin/view/', AdminChangeGenericAPIView.as_view()),
]