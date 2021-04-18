from rest_framework import serializers
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = '__all__'


class PostDetailSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    comments = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'link',
            'author',
            'created',
            'comments',
        ]


class PostCreateSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'link',
            'author',
            'created',
        ]


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title'
        ]
