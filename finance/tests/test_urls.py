from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from finance.views import FinancialStatementListAPIView

class TestUrls(SimpleTestCase):
  def test_finance_list_url_is_resolved(self):
    url = reverse('finance-list')
    self.assertEqual(resolve(url).func.view_class, FinancialStatementListAPIView)