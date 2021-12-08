from django.db.models import fields
from rest_framework import serializers
from.models import Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ('user','school_name ', 'rating','comment')