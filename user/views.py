from rest_framework import generics, status, response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from user import models, serializers as user_ser


class MyTokenObtainPairView(TokenObtainPairView):
    """
    JWT Custom Token Claims View
    """
    serializer_class = user_ser.CustomTokenObtainPairSerializer
    token_obtain_pair = TokenObtainPairView.as_view()


class NewUserView(generics.ListCreateAPIView):
    """
    New User Create View
    """
    serializer_class = user_ser.NewUserSerializer
    queryset = models.User.objects.all()
    # permission_classes = [apipermissions.IsSuperUser]

    def create(self, request, *args, **kwargs):
        user = request.data
        ser = self.serializer_class(data=user)
        ser.is_valid(raise_exception=True)
        new_user = ser.save()
        user_data = ser.data
        tokens = RefreshToken.for_user(new_user)
        refresh = str(tokens)
        access = str(tokens.access_token)

        return response.Response({'user_data': user_data, 'refresh_token': refresh, 'access_token': access},
                                 status=status.HTTP_201_CREATED)

