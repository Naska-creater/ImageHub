from django.urls import path

from image.views import (CategoryGenericAPIView, ImageGenericAPIView, CategoryChangeGenericAPIView,
                         CategoryCreateGenericAPIView)

urlpatterns = [
    path('category/change/<int:pk>/', CategoryChangeGenericAPIView.as_view()),
    path('category/create/', CategoryCreateGenericAPIView.as_view()),
    path('categories/', CategoryGenericAPIView.as_view()),
    path('images/', ImageGenericAPIView.as_view()),
]