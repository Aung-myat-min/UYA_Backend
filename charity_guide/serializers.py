from rest_framework import serializers
from .models import CharityGuide, CharityImage
from django.conf import settings

class CharityImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = CharityImage
        fields = "__all__"

    def get_image(self, obj):
        if obj.image:
            return f"https://res.cloudinary.com/{settings.CLOUDINARY_CLOUD_NAME}/{obj.image}"
        return None
class CharityGuideSerializer(serializers.ModelSerializer):
    images = CharityImageSerializer(many=True, read_only=True)

    class Meta:
        model = CharityGuide
        fields = "__all__"
    
