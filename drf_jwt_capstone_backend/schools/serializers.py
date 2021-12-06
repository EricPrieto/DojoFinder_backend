from rest_framework import serializers
from.models import School



class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('user', 'school_type', 'school_name ',
                  'address', 'zip_code ', 'phone', 'school_description')



           