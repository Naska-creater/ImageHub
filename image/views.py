from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from image.models import Category, Image
from image.serializers import CategorySerializer, ImageViewSerializer, CategoryChangeSerializer, ImageCreateSerializer, \
    ImageChangeSerializer

from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser


class CategoryGenericAPIView(GenericAPIView, ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_description='Просмотр всех категорий авторизованным пользователем',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class CategoryChangeGenericAPIView(GenericAPIView,DestroyModelMixin,UpdateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryChangeSerializer
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(
        operation_description='Удаление категорий администратором приложения',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Изменение категорий администратором приложения',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class CategoryCreateGenericAPIView(GenericAPIView,CreateModelMixin,ListModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategoryChangeSerializer
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(
        operation_description='Просмотр всех категорий администратором приложения',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Создание новых категорий администратором приложения',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ImageGenericAPIView(GenericAPIView, ListModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageViewSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_description='Просмотр все картинок и их полей для авторизованного пользователя',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ImageCreateGenericAPIView(GenericAPIView, CreateModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @swagger_auto_schema(
        operation_description='Загрузка картинок авторизованным пользователем',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ImageChangeGenericAPIView(GenericAPIView, DestroyModelMixin, UpdateModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageChangeSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_description='Удаление картинок, загруженных авторизованным пользователем',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def delete(self, request, *args, **kwargs):
        image = self.get_object()
        if image.user != request.user:
            return Response({"detail": "У Вас нет прав на изменение этого изображения."}, status=403)
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Изменение полей картинок, загруженных авторизованным пользователем',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def patch(self, request, *args, **kwargs):
        image = self.get_object()
        if image.user != request.user:
            return Response({"detail": "У Вас нет прав на изменение этого изображения."}, status=403)
        return self.partial_update(request, *args, **kwargs)

class MyImageGenericAPIView(GenericAPIView,ListModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageChangeSerializer
    permission_classes = (IsAuthenticated,)

    @swagger_auto_schema(
        operation_description='Возвращает все картинки, загруженные авторизованным пользователем',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def get(self, request, *args, **kwargs):
        self.queryset=self.queryset.filter(user=request.user)
        return self.list(request, *args, **kwargs)

class ImageAdminChangeGenericAPIView(GenericAPIView,DestroyModelMixin,UpdateModelMixin):
    queryset = Image.objects.all()
    serializer_class = ImageChangeSerializer
    permission_classes = (IsAdminUser,)

    @swagger_auto_schema(
        operation_description='Удаление картинок любого пользователя администратором',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Изменение описаний все загруженных картинок администратором',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)