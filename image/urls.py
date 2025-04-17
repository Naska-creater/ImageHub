from django.urls import path

from image.views import (CategoryGenericAPIView, ImageGenericAPIView, CategoryChangeGenericAPIView,
                         CategoryCreateGenericAPIView, ImageCreateGenericAPIView, ImageChangeGenericAPIView,
                         MyImageGenericAPIView, ImageAdminChangeGenericAPIView)

urlpatterns = [
    path('category/change/<int:pk>/', CategoryChangeGenericAPIView.as_view()),
    path('category/create/', CategoryCreateGenericAPIView.as_view()),
    path('categories/', CategoryGenericAPIView.as_view()),
    path('images/', ImageGenericAPIView.as_view()),
    path('create/', ImageCreateGenericAPIView.as_view()),
    path('change/<int:pk>/', ImageChangeGenericAPIView.as_view()),
    path('my/', MyImageGenericAPIView.as_view()),
    path('admin/change/<int:pk>/', ImageAdminChangeGenericAPIView.as_view()),

]