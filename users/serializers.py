from rest_framework import serializers

from users.models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    """ Сериализатор для регистрации пользователя """
    class Meta:
        model = User
        fields = ('email', 'password',)


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор для изменения провиля и удаления пользователя """
    class Meta:
        model = User
        fields = '__all__'
