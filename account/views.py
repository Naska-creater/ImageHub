from django.core.serializers import serialize
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.permissions import IsAuthenticated

from account.models import User
from account.serializers import UserSerializerRegister, UsersSerializer


class UserRegistrationGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UserSerializerRegister

    def post (self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class UsersGenericAPIView(GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = (IsAuthenticated, )

    def get (self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def patch (self, request, *args, **kwargs):
    #     return self.partial_update(request, *args, **kwargs)
