from rest_framework import serializers

from Profile.models import Profiles

class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profiles
        fields = ('__all__')        