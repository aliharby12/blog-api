from rest_framework.serializers import (ModelSerializer,
                                        HyperlinkedIdentityField)


from blogapp.models import Post


class PostListSerializer(ModelSerializer):
    detail_link = HyperlinkedIdentityField(view_name = 'api-detail')
    class Meta:
        model = Post
        fields = 'detail_link', 'id', 'author', 'title', 'content'

        def get_user(self, obj):
            return str(obj.user.username)

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
