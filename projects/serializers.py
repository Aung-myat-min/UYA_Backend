from rest_framework import serializers
from .models import Project, ProjectImage
from django.conf import settings

class ProjectImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    class Meta:
        model = ProjectImage
        fields = "__all__"
    
    def get_image(self, obj):
        if obj.image:
            return f"https://res.cloudinary.com/{settings.CLOUDINARY_CLOUD_NAME}/{obj.image}"
        return None


class ProjectSerializer(serializers.ModelSerializer):
    images = ProjectImageSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = "__all__"