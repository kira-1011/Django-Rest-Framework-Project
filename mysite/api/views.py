from django.shortcuts import render
from rest_framework import generics, response, status, views
from .serializers import BlogPostSerializer
from .models import BlogPost
from rest_framework.decorators import action

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        '''
        Delete all blog posts
        '''
        BlogPost.objects.all().delete()
        return response.Response(status=status.HTTP_204_NO_CONTENT)

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'pk'