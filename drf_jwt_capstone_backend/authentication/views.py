from django.contrib.auth import get_user_model
from .serializers import RegistrationSerializer
from .serializers import UserSerializer
from rest_framework import generics, serializers
from rest_framework.permissions import AllowAny
User = get_user_model()
from rest_framework import status
from rest_framework.views import APIView
from django.http.response import Http404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer

class UserDetail(APIView):
    permission_classes = (IsAuthenticated)

    def get_object_by_username(self, userName):
        try:
            return User.objects.filter(userName = userName)
        except User.DoesNotExist:
            raise Http404
    
    def get_object(self, pk):
        try:
            return User.objects.get(pk =pk)
        except User.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user= self.get.object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def get_by_userName(self, userName):
        user = self.get_object_by_username(userName)
        serializer = UserSerializer(user)
        return Response(serializer.data)

class UserList(APIView):

    def get(self):
        users = self.get_object.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)