from rest_framework.generics import GenericAPIView, DestroyAPIView

from image.models import Category, Image
from image.serializers import CategorySerializer, ImageSerializer

from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CategoryGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

class CategoryCreateGenericAPIView(GenericAPIView, ListModelMixin,CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminUser,)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class ImageGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (IsAuthenticated,)

