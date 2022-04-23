from rest_framework import generics, permissions

# from BitBlog.paginations import CustomPagination
from .models import Post
from .serializers import PostSerializer


class PostList(generics.ListAPIView):

    # pagination_class = CustomPagination
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
