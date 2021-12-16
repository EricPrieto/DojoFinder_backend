from django.shortcuts import render
from rest_framework import serializers
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import School
from .serializers import SchoolSerializer
# from .models import Rating
# from .serializers import RatingSerializer
from django.contrib.auth.models import User
from django.http.response import Http404
from rest_framework.decorators import action


# Create your views here.

class SchoolList(APIView):
    permission_classes = (IsAuthenticated)
    def get(self, request):
        schools = School.objects.all()
        serializer = SchoolSerializer(schools, many=True)
        return Response(Serializer.data)
    
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action (detail=True, methods=['POST'])
    def rate_school(self, request, pk=None):
        if 'stars' in request.data:
            
            school = School.objects.get(id=pk)
            stars = request.data['stars']
            # user = request.user
            # user = User.objects.get(id=1)
            
            try:
                rating = Rating.objects.get(user=id, school=school.id)
                rating.stars = stars
                rating.save()
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating updated', 'result' : serializer.data}
                return Response (response, status=status.HTTP_200_OK)

            except:
                rating = Rating.objects.get(user=User, school=school, stars=stars)
                serializer = RatingSerializer(rating, many=False)
                response = {'message': 'Rating created', 'result' : serializer.data}
                return Response (response, status=status.HTTP_200_OK)
                
        else:
            response = {'message': 'Stars need to be provided'}
            return Response (response, status=status.HTTP_400_BAD_REQUEST)

class RatingView(APIView):
    permission_classes = (IsAuthenticated)

    def get(self, request):
        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)
        return Response(serializer.data)



