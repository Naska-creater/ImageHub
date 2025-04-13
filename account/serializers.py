from rest_framework import serializers

from account.models import User


class UserSerializerRegister(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'second_name', 'email','phone', 'password','nick_name']
        extra_kwargs = {'password': {'write_only':True}}

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['nick_name']
