from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from charity_guide.views import CharityGuideListAPIView, CharityGuideDetailAPIView, CharityGuideByRegionAPIView

class TestUrls(SimpleTestCase):
    def test_charity_list_url_is_resolved(self):
        url = reverse('charity-list')
        self.assertEqual(resolve(url).func.view_class, CharityGuideListAPIView)
  
    def test_charity_detail_url_is_resolved(self):
        url = reverse('charity-detail', args=[1]) 
        self.assertEqual(resolve(url).func.view_class, CharityGuideDetailAPIView)
  
    def test_charity_by_region_url_is_resolved(self):
        url = reverse('charity-by-region', args=['Yangon'])
        self.assertEqual(resolve(url).func.view_class, CharityGuideByRegionAPIView)
