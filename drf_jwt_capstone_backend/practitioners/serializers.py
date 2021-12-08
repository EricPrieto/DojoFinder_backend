from rest_framework import serializers
from.models import Practitioner



class PractitionerSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Practitioner
        # If added new columns through the User model, add them in the fields
        # list as seen below
        fields = ('user', 'first_name', 'last_name ', 'middle_initial',
                  'address', 'zip_code', 'phone','school_interest')



       