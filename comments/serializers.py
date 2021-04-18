from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer,
    ReadOnlyField,
)

from accounts.serializers import UserDetailSerializer
from comments.models import Comment


class CommentCreateSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = [
            'content',
            'author',
            'post',
        ]


class CommentSerializer(ModelSerializer):
    reply_count = SerializerMethodField()
    author = UserDetailSerializer()

    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'post',
            'content',
            'parent',
            'reply_count',
            'created',
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0


class CommentChildSerializer(ModelSerializer):
    author = UserDetailSerializer()

    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'content',
            'created',
        ]


class CommentDetailSerializer(ModelSerializer):
    reply_count = SerializerMethodField()
    replies = SerializerMethodField()
    author = UserDetailSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            'id',
            'author',
            'post',
            'content',
            'reply_count',
            'replies',
            'created',
        ]
        read_only_fields = [
            'post',
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentChildSerializer(obj.children(), many=True).data
        return None
