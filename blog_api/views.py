from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import DjangoModelPermissions


class PostList(generics.ListCreateAPIView):
    permission_classes = [DjangoModelPermissions]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    pass


class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
