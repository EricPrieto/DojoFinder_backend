from django.db.models import fields
from rest_framework import serializers
from.models import Rating


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('id', 'user', 'stars', 'rated_school ')

