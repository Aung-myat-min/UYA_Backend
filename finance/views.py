from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from .models import FinancialStatement
from .serializers import FinancialStatementSerializer

class FinancialStatementListAPIView(APIView):
    def get(self, request):
        statements = FinancialStatement.objects.filter(is_published=True).order_by('-release_date')
        serializer = FinancialStatementSerializer(statements, many=True)
        return Response({
            "meta": {
                "message": "Financial statements retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "self": request.build_absolute_uri(),
            }
        }, status=status.HTTP_200_OK)
