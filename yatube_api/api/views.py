from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from api.permissions import IsOwnerOrReadOnly
from api.serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer
)
from posts.models import Group, Post


class BasePermissionViewSet(viewsets.ModelViewSet):
    """Базовый класс с общими настройками прав доступа."""

    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class PostViewSet(BasePermissionViewSet):
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Post.objects.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(BasePermissionViewSet):
    serializer_class = CommentSerializer

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (AllowAny,)


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    serializer_class = FollowSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('following__username',)

    def get_user(self):
        return self.request.user

    def get_queryset(self):
        return self.get_user().follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.get_user())
