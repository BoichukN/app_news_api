from django.contrib.auth import get_user_model

from rest_framework.serializers import (
    CharField,
    ModelSerializer,
    ValidationError
)

User = get_user_model()


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            'username',
        ]


class UserCreateSerializer(ModelSerializer):
    username = CharField(max_length=50)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        username = data['username']
        user_qs = User.objects.filter(username=username)
        if user_qs.exists():
            raise ValidationError("This user has already registered.")
        return data

    def create(self, validated_data):
        username = validated_data['username']
        password = validated_data['password']
        user_obj = User(username=username,)
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)
    username = CharField(max_length=50)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
        ]
        extra_kwargs = {"password": {"write_only": True}}
