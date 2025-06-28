from rest_framework import serializers
from .models import CharityGuide, CharityImage

class CharityImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = CharityImage
        fields = "__all__"

class CharityGuideSerializer(serializers.ModelSerializer):
    images = CharityImageSerializer(many=True, read_only=True)

    class Meta:
        model = CharityGuide
        fields = "__all__"
    
