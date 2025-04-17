from django.core.serializers import serialize
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from account.models import User
from account.serializers import UserSerializerRegister, UsersSerializer


class UserRegistrationGenericAPIView(GenericAPIView, CreateModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializerRegister

    def post (self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UserChangeGenericAPIView(GenericAPIView,RetrieveModelMixin, UpdateModelMixin,DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated, )

    def get_object(self):
        return self.request.user

    def get (self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch (self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete (self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class AdminChangeGenericAPIView(GenericAPIView,ListModelMixin, UpdateModelMixin,DestroyModelMixin):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAdminUser, )

    def get (self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def patch (self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete (self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
