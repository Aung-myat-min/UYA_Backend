from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FinancialStatement
from .serializers import FinancialStatementSerializer

class FinancialStatementListView(APIView):
    def get(self, request):
        statements = FinancialStatement.objects.all().order_by('-release_date').filter(is_published=True)
        serializer = FinancialStatementSerializer(statements, many=True)
        return Response({
            "status": "success",
            "data": serializer.data,
            "message": "Financial statements retrieved successfully"
        }, status=status.HTTP_200_OK)
        