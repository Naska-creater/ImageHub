from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from account.models import User
from account.serializers import UserSerializerRegister, UsersSerializer


class UserRegistrationGenericAPIView(GenericAPIView, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializerRegister

    @swagger_auto_schema(
        operation_description='Регистрация аккаута пользователем',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def post (self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserChangeGenericAPIView(GenericAPIView,RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user

    @swagger_auto_schema(
        operation_description='Просмотр своего аккаута пользователем',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def get (self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Изменение полей своего аккаута пользователем',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def patch (self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Удаление своего аккаута пользователем',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def delete (self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AdminChangeGenericAPIView(GenericAPIView,ListModelMixin, UpdateModelMixin,DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAdminUser, )

    @swagger_auto_schema(
        operation_description='Просмотр всех аккаутов пользователей администратором приложения',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def get (self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Изменение полей аккаута пользователя администратором приложения',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def patch (self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description='Удаление аккаута пользователя администратором приложения',
        responses={200: openapi.Response("OK", openapi.Schema(type=openapi.TYPE_OBJECT))}
    )
    def delete (self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
