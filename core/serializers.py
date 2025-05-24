from rest_framework import serializers
from .models import SocialPlatform, PartnerOrganization

class SocialPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPlatform
        fields = "__all__"
class PartnerOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerOrganization
        fields = "__all__"
