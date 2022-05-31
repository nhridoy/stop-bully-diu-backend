from django.shortcuts import render
from complain import serializers as complain_ser, models as complain_model
from rest_framework import generics, permissions


# Create your views here.
class ComplainView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = complain_ser.ComplainSerializer
    queryset = complain_model.ComplainModel.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ComplainListView(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = complain_ser.ComplainSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = complain_model.ComplainModel.objects.all()
        else:
            queryset = complain_model.ComplainModel.objects.filter(user_id=self.request.user.id)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ComplainStatusView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAdminUser]
    serializer_class = complain_ser.ComplainStatusSerializer
    queryset = complain_model.ComplainModel.objects.all()
    lookup_field = 'id'

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


