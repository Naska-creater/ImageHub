from rest_framework import status
from rest_framework.generics import GenericAPIView, DestroyAPIView
from rest_framework.response import Response

from image.models import Category, Image
from image.serializers import CategorySerializer, ImageSerializer, CategoryChangeSerializer

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CategoryGenericAPIView(GenericAPIView, ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class CategoryChangeGenericAPIView(GenericAPIView,DestroyModelMixin,UpdateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryChangeSerializer
    permission_classes = (IsAdminUser,)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class CategoryCreateGenericAPIView(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryChangeSerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ImageGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,)

