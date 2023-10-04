from rest_framework import serializers

from .models import OrganizationDetails


class OrganizationDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationDetails
        fields = '__all__'
