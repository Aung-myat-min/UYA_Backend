from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SocialPlatform, PartnerOrganization, ActivityPhoto
from .serializers import SocialPlatformSerializer, PartnerOrganizationSerializer, ActivityPhotoSerializer

class PartnerOrganizationListAPIView(APIView):
    def get(self, request):
        partners = SocialPlatform.objects.all()
        serializer = SocialPlatformSerializer(partners, many=True)
        return Response({
            "status": "success",
            "message": "Partner organizations retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
class PartnerOrganizationListAPIView(APIView):
    def get(self, request):
        partners = PartnerOrganization.objects.all()
        serializer = PartnerOrganizationSerializer(partners, many=True)
        return Response({
            "status": "success",
            "message": "Partner organizations retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class ActivityPhotoListAPIView(APIView):
    def get(self, request):
        photos = ActivityPhoto.objects.all().order_by('-uploaded_at')
        serializer = ActivityPhotoSerializer(photos, many=True)
        return Response({
            "status": "success",
            "message": "Activity photos retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
