from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SocialPlatform, PartnerOrganization, ActivityPhoto, DonationCertificate
from .serializers import SocialPlatformSerializer, PartnerOrganizationSerializer, ActivityPhotoSerializer, DonationCertificateSerializer
from django.shortcuts import render
from datetime import datetime
from django.urls import reverse

class SocialPlatformListAPIView(APIView):
    def get(self, request):
        platforms = SocialPlatform.objects.all()
        serializer = SocialPlatformSerializer(platforms, many=True)
        return Response({
            "meta": {
                "message": "Social platforms retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "partners":request.build_absolute_uri(reverse('partner-orgs-list')),
                "activities":request.build_absolute_uri(reverse('activity-photo-list')),
                "platforms":request.build_absolute_uri(reverse('social-platforms-list')),
                "certificates":request.build_absolute_uri(reverse('certificates-list')),
            }
        }, status=status.HTTP_200_OK)


class PartnerOrganizationListAPIView(APIView):
    def get(self, request):
        partners = PartnerOrganization.objects.all()
        serializer = PartnerOrganizationSerializer(partners, many=True)
        return Response({
            "meta": {
                "message": "Partner organizations retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "partners":request.build_absolute_uri(reverse('partner-orgs-list')),
                "activities":request.build_absolute_uri(reverse('activity-photo-list')),
                "platforms":request.build_absolute_uri(reverse('social-platforms-list')),
                "certificates":request.build_absolute_uri(reverse('certificates-list')),
            }
        }, status=status.HTTP_200_OK)


class ActivityPhotoListAPIView(APIView):
    def get(self, request):
        photos = ActivityPhoto.objects.all().order_by('-uploaded_at')
        serializer = ActivityPhotoSerializer(photos, many=True)
        return Response({
            "meta": {
                "message": "Activity photos retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "partners":request.build_absolute_uri(reverse('partner-orgs-list')),
                "activities":request.build_absolute_uri(reverse('activity-photo-list')),
                "platforms":request.build_absolute_uri(reverse('social-platforms-list')),
                "certificates":request.build_absolute_uri(reverse('certificates-list')),
            }
        }, status=status.HTTP_200_OK)


def terms_view(request):
    return render(request, "terms_of_service.html", {"now": datetime.now()})
class DonationCertificateListAPIView(APIView):
    def get(self, request):
        certificates = DonationCertificate.objects.all().order_by('-uploaded_at')
        serializer = DonationCertificateSerializer(certificates, many=True)
        return Response({
            "meta": {
                "message": "Donation certificates retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "partners":request.build_absolute_uri(reverse('partner-orgs-list')),
                "activities":request.build_absolute_uri(reverse('activity-photo-list')),
                "platforms":request.build_absolute_uri(reverse('social-platforms-list')),
                "certificates":request.build_absolute_uri(reverse('certificates-list')),
            }
        }, status=status.HTTP_200_OK)

