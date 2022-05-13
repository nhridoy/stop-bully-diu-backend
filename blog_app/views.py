import random
import base64
from django.shortcuts import render
from rest_framework import generics, permissions
from blog_app import models as blog_model, serializers as blog_ser
from user import apipermissions as user_per


# Create your views here.
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
