from rest_framework import serializers
from .models import SocialPlatform, PartnerOrganization, ActivityPhoto, DonationCertificate

class SocialPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPlatform
        fields = "__all__"
class PartnerOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartnerOrganization
        fields = "__all__"
class ActivityPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPhoto
        fields = '__all__'
        
class DonationCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationCertificate
        fields = '__all__'

