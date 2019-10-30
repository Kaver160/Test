from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import generics
from backend.app.models import Post

class PostListSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id','user','text')

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        user = serializers.HiddenField(default=serializers.CurrentUserDefault())#при каждом создание пользователь должен сам создаваться, и теперь если ты не авторизован как пользователь ты не сможешь не чего изменить не чего
        model = Post
        fields = '__all__' # что мы хотим сериализовать все поля, Работа со всеми полями

class UserSerialiser(serializers.ModelSerializer):
    """Сериализация пользователя"""
    class Meta:
        model = User
        fields = ("id", "username")
class PostSerializer(serializers.ModelSerializer):
    """Serializer твитов"""
    user = UserSerialiser()
    user_like = UserSerialiser(many=True)
    class Meta:
        model = Post
        fields = ("id",
                  "user",
                  "text",
                  "date",
                  "twit",
                  "like",
                  "user_like")
#
#
# class AddTweetSerializer(serializers.ModelSerializer):
#     """Добавление твита"""
#     class Meta:
#         model = Post
#         fields = ("text", )
#
# class PostDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = '__all__'
# class EditTwit(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ("text", )