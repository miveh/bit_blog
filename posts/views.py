from rest_framework import generics, permissions

from BitBlog.paginations import CustomPagination
from .models import Post
from .serializers import PostSerializer, RateCreateSerializer


class PostList(generics.ListAPIView):
    """
        API for create rates
    """

    pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class RatesCreateAPIView(generics.CreateAPIView):
    """
        API for create rates
    """

    permission_classes = [permissions.IsAuthenticated]
    serializer_class = RateCreateSerializer
