from rest_framework import serializers
from .models import SocialPlatform, PartnerOrganization, ActivityPhoto, DonationCertificate
from django.conf import settings
class SocialPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPlatform
        fields = "__all__"
class PartnerOrganizationSerializer(serializers.ModelSerializer):
    logo = serializers.SerializerMethodField()
    class Meta:
        model = PartnerOrganization
        fields = "__all__"
    
    def get_logo(self, obj):
        if obj.logo:
            return f"https://res.cloudinary.com/{settings.CLOUDINARY_CLOUD_NAME}/{obj.logo}"
        return None
class ActivityPhotoSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = ActivityPhoto
        fields = '__all__'
    
    def get_image(self, obj):
        if obj.image:
            return f"https://res.cloudinary.com/{settings.CLOUDINARY_CLOUD_NAME}/{obj.image}"
        return None
class DonationCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationCertificate
        fields = '__all__'

    def get_certificate(self, obj):
        if obj.certificate:
            return f"https://res.cloudinary.com/{settings.CLOUDINARY_CLOUD_NAME}/{obj.certificate}"
        return None
