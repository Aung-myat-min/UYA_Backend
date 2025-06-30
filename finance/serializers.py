from rest_framework import serializers
from .models import FinancialStatement

class FinancialStatementSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinancialStatement
        fields = "__all__"
