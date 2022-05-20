import random
import base64
from django.shortcuts import render
from rest_framework import generics, permissions
from blog_app import models as blog_model, serializers as blog_ser
from user import apipermissions as user_per


# Create your views here.

class BlogTagsView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = blog_ser.BlogTagsSerializer
    queryset = blog_model.BlogTagsModel.objects.all()


class BlogPostView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = blog_ser.BlogSerializer
    queryset = blog_model.BlogModel.objects.all()

    def perform_create(self, serializer):
        rand_num = random.randint(99, 222)
        blog_slug_str = f"{serializer.validated_data.get('blogtitle')}{rand_num}"
        sample_string_bytes = blog_slug_str.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        slug = base64_bytes.decode("ascii")
        serializer.save(user=self.request.user, slug=slug)


class BlogPostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = blog_ser.BlogSerializer
    queryset = blog_model.BlogModel.objects.all()
    lookup_field = 'id'


class ForumCategoriesView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = blog_ser.ForumCategoriesSerializer
    queryset = blog_model.ForumCategoryModel.objects.all()


class ForumPostView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = blog_ser.ForumSerializer
    queryset = blog_model.ForumModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ForumCommentView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = blog_ser.ForumCommentSerializer
    queryset = blog_model.ForumCommentModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, forum_post=blog_model.ForumModel.objects.get(id=self.kwargs['forum_id']))


class ForumPostUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = blog_ser.ForumSerializer
    queryset = blog_model.ForumModel.objects.all()
    lookup_field = 'id'
