from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import PartnerOrganization
from .serializers import PartnerOrganizationSerializer

class PartnerOrganizationListAPIView(APIView):
    def get(self, request):
        partners = PartnerOrganization.objects.all()
        serializer = PartnerOrganizationSerializer(partners, many=True)
        return Response({
            "status": "success",
            "message": "Partner organizations retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
