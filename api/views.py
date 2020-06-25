from rest_framework.generics import (ListAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveAPIView,
                                     CreateAPIView)
                                     
from blogapp.models import Post
from django.shortcuts import get_object_or_404
from .serializers import (PostListSerializer,
                          PostCreateSerializer,
                          PostDetailSerializer,
                          PostUpdateSerializer)

from rest_framework.permissions import (AllowAny,
                                        IsAuthenticated,
                                        IsAdminUser,
                                        IsAuthenticatedOrReadOnly)
from .permissions import IsOwnerOrReadOnly



class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailSerializer




    def delete(self, request, id):
        queryset = get_object_or_404(Post, id = id)
        queryset.delete()


class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostUpdateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
