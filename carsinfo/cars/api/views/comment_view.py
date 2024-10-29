from cars.models import Comment
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from cars.api.serializers.comment_serializer import CreateCommentSerializer, CommentSerializer


class CommentView(generics.ListCreateAPIView):
    """Просмотр и создание комментариев."""

    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CreateCommentSerializer
        return CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.filter(car=self.kwargs.get('pk'))
        return queryset

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, car_id=self.kwargs.get('pk'))