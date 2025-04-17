from rest_framework import serializers

from account.models import User


class UserSerializerRegister(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'second_name', 'email','phone', 'password','nick_name']
        extra_kwargs = {'password': {'write_only':True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
