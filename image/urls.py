from django.urls import path

from image.views import CategoryGenericAPIView, CategoryCreateGenericAPIView, ImageGenericAPIView

urlpatterns = [
    path('category/create/', CategoryCreateGenericAPIView.as_view()),
    path('categories/', CategoryGenericAPIView.as_view()),
    path('images/', ImageGenericAPIView.as_view()),
]