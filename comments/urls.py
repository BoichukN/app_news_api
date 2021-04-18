from django.urls import path

from .views import (
    CommentCreateAPIView,
    CommentDetailAPIView,
    CommentListAPIView,

)

urlpatterns = [
    path('', CommentListAPIView.as_view(), name='comments_list'),
    path('create/', CommentCreateAPIView.as_view(), name='comment_create'),
    path('<int:pk>/', CommentDetailAPIView.as_view(), name='comment_detail'),
]
