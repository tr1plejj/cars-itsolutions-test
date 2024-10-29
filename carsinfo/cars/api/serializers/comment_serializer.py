from rest_framework import serializers
from cars.models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    class Meta:
        model = Comment
        exclude = (
            'id',
            'car',
        )

class CreateCommentSerializer(serializers.ModelSerializer):
    """Сериализатор для создания комментариев."""


    class Meta:
        model = Comment
        fields = (
            'content',
        )