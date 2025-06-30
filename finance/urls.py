from django.urls import path
from .views import FinancialStatementListAPIView

urlpatterns = [
    path('finances/', FinancialStatementListAPIView.as_view(), name='finance-list'),
]
