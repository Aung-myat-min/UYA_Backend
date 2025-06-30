from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from finance.views import FinancialStatementListAPIView
from rest_framework.test import APITestCase
from rest_framework import status
from .models import FinancialStatement
from datetime import date

class TestUrls(SimpleTestCase):
  def test_finance_list_url_is_resolved(self):
    url = reverse('finance-list')
    self.assertEqual(resolve(url).func.view_class, FinancialStatementListAPIView)

class TestFinancialStatementAPI(APITestCase):
    def setUp(self):
        # Published statement
        self.statement1 = FinancialStatement.objects.create(
            statement_name="Q1 Report",
            release_date=date(2024, 4, 1),
            statement_link="https://example.com/q1",
            is_published=True
        )

        # Unpublished statement
        self.statement2 = FinancialStatement.objects.create(
            statement_name="Q2 Draft",
            release_date=date(2024, 5, 1),
            statement_link="https://example.com/q2",
            is_published=False
        )

    def test_get_published_financial_statements(self):
        url = reverse('finance-list')  
        response = self.client.get(url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'success')
        self.assertEqual(len(response.data['data']), 1)  
        self.assertEqual(response.data['data'][0]['statement_name'], "Q1 Report")
