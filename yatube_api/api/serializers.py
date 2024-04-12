from rest_framework import serializers

from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'pub_date', 'author', 'image', 'group',
        )


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = (
            'id', 'title', 'slug', 'description',
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True,
                                          slug_field='username')
    group = serializers.SlugRelatedField(read_only=True,
                                         slug_field='title')

    class Meta:
        model = Comment
        fields = (
            'id', 'author', 'post', 'text', 'created',
        )
