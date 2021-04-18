from django.urls import path

from .views import (
    PostsListAPIView,
    PostCreateAPIView,
    PostDetailAPIView,
    PostUpdateAPIView,
    PostDeleteAPIView,
)

urlpatterns = [
    path('', PostsListAPIView.as_view(), name='posts_list'),
    path('create/', PostCreateAPIView.as_view(), name='post_create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name='post_detail'),
    path('<int:pk>/edit/', PostUpdateAPIView.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='post_delete')
]
