from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)
from rest_framework.response import Response

from posts.models import Post
from posts.permissions import IsOwnerOrReadOnly
from comments.models import Comment
from .serializers import (
    CommentCreateSerializer,
    CommentSerializer,
    CommentDetailSerializer,
)


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, pk):
        try:
            post = get_object_or_404(Post, pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if request.method == 'POST':
            serializer = CommentCreateSerializer(data=request.data, context={'request': request})
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    permission_classes = [IsOwnerOrReadOnly]


class CommentListAPIView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get(self, request, pk):
        try:
            post = get_object_or_404(Post, pk=pk)
        except Post.DoesNotExist:
            return Response(status=status.HTTP_404_Not_Found)
        if request.method == 'GET':
            comments = Comment.objects.filter(post=post)
            serializers = CommentSerializer(comments, many=True)
            return Response(serializers.data)
