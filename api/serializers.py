from rest_framework.serializers import ModelSerializer
from blogapp.models import Post


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = 'id', 'author', 'title', 'content'

class PostDetailSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = 'id', 'author', 'title', 'content', 'date_posted'

class PostCreateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = 'title', 'content'

class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = 'title', 'content'
