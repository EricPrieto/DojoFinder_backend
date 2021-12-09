from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Rating
from .serializers import RatingSerializer
from django.contrib.auth.models import User
from django.http.response import Http404

# Create your views here.


class RatingView(APIView):
    permission_classes = (IsAuthenticated)

    def get(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer
        return Response(Serializer.data)
