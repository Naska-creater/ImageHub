from rest_framework import serializers

from image.models import Category, Image


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name']

class CategoryChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ImageViewSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.nick_name', read_only=True)
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Image
        fields = ('file', 'description','user','category')

class ImageCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields =('file', 'description','category','user')
        read_only_fields = ('user',)

class ImageChangeSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')

    class Meta:
        model = Image
        fields = ('id', 'file', 'description','category')