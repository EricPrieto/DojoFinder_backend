from django.shortcuts import render
from rest_framework import status
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Practitioner
from .serializers import PractitionerSerializer
from django.contrib.auth.models import User
from django.http.response import Http404

# Create your views here.

class PractitionerList(APIView):
    permission_classes = (IsAuthenticated)

    def get(self, request):
        schools = Practitioner.objects.all()
        serializer = PractitionerSerializer(schools, many=True)
        return Response(Serializer.data)

