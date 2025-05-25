from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CharityGuide, CharityImage
from .serializers import CharityGuideSerializer, CharityImageSerializer

class CharityGuideListAPIView(APIView):
    def get(self, request):
        charities = CharityGuide.objects.prefetch_related('images').filter(is_published=True).order_by('-created_at')
        serializer = CharityGuideSerializer(charities, many=True)
        return Response({
            "status": "success",
            "message": "Charity list retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class CharityGuideDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            charity = CharityGuide.objects.prefetch_related('images').get(pk=pk, is_published=True)
        except CharityGuide.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Charity not found",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = CharityGuideSerializer(charity)
        return Response({
            "status": "success",
            "message": "Charity detail retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class CharityGuideByRegionAPIView(APIView):
    def get(self, request, region_name):
        charities = CharityGuide.objects.prefetch_related('images').filter(
            is_published=True,
            region=region_name
        )
        serializer = CharityGuideSerializer(charities, many=True)
        return Response({
            "status": "success",
            "message": f"Charities in {region_name} retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
