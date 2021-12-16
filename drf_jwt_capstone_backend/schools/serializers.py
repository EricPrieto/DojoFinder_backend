from django.db.models import fields
from rest_framework import serializers
from.models import School



class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('id', 'user', 'school_type', 'school_name ', 'school_address', 
                'school_zip', 'phone', 'school_description', 'rating', 'image', 'no_of_ratings', 'avg_rating')


# class RatingSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Rating
#         # If added new columns through the User model, add them in the fields
#         # list as seen below
#         fields = ('id', 'user', 'stars', 'school')






