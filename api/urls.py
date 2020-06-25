from django.urls import path
from .views import PostListAPIView, PostCreateAPIView, PostDetailAPIView, PostUpdateAPIView


urlpatterns = [
    path('', PostListAPIView.as_view(), name = 'api-list'),
    path('create', PostCreateAPIView.as_view(), name = 'api-create'),
    path('<int:pk>/', PostDetailAPIView.as_view(), name = 'api-detail'),
    path('<int:pk>/update', PostUpdateAPIView.as_view(), name = 'api-update'),
]
