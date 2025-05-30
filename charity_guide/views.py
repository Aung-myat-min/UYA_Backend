from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from .models import CharityGuide
from .serializers import CharityGuideSerializer


class CharityGuideListAPIView(APIView):
    def get(self, request):
        charities = CharityGuide.objects.prefetch_related('images').filter(is_published=True).order_by('-created_at')
        serializer = CharityGuideSerializer(charities, many=True)
        return Response({
            "meta": {
                "message": "Charity list retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "self": request.build_absolute_uri(),
                "detail": request.build_absolute_uri(reverse("charity-detail", args=[1])), 
                "by_region": request.build_absolute_uri(reverse("charity-by-region", args=["Yangon"])) 
            }
        }, status=status.HTTP_200_OK)


class CharityGuideDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            charity = CharityGuide.objects.prefetch_related('images').get(pk=pk, is_published=True)
        except CharityGuide.DoesNotExist:
            return Response({
                "meta": {
                    "message": "Charity not found",
                    "status_code": status.HTTP_404_NOT_FOUND
                },
                "data": None,
                "links": {
                    "self": request.build_absolute_uri(),
                    "list": request.build_absolute_uri(reverse("charity-list")), 
                    "by_region": request.build_absolute_uri(reverse("charity-by-region", args=["Yangon"])) 
                }
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = CharityGuideSerializer(charity)
        return Response({
            "meta": {
                "message": "Charity detail retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "self": request.build_absolute_uri(),
                "list": request.build_absolute_uri(reverse("charity-list")), 
                "by_region": request.build_absolute_uri(reverse("charity-by-region", args=["Yangon"])) 
            }
        }, status=status.HTTP_200_OK)


class CharityGuideByRegionAPIView(APIView):
    def get(self, request, region_name):
        charities = CharityGuide.objects.prefetch_related('images').filter(
            is_published=True,
            region=region_name
        )
        serializer = CharityGuideSerializer(charities, many=True)
        return Response({
            "meta": {
                "message": f"Charities in {region_name} retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "self": request.build_absolute_uri(),
                "list": request.build_absolute_uri(reverse("charityguide-list")),
                "detail": request.build_absolute_uri(reverse("charity-detail", args=[1])), 
            }
        }, status=status.HTTP_200_OK)
