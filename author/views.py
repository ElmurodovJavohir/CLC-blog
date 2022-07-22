from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from author.models import Author
from post.models import Post
from post.serializer import PostSerializer
from author.serializer import AuthorDetailSerializer
from helpers.pagination import CustomPagination
"""
TODO:
    - AUTHOR DETAIL
    - AUTHOR DETAIL POST
"""


class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorDetailSerializer
    lookup_field = 'id'

class AuthorDetailView(generics.CreateAPIView):
    queryset = ContantUs.objects.all()
    serializer_class = Contactus




class AuthorPostsView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        queryset = self.queryset
        if self.kwargs.get('author_id', None):
            queryset = queryset.filter(author__id=self.kwargs['author_id'])

        return queryset
