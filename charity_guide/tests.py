from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from charity_guide.views import CharityGuideListAPIView, CharityGuideDetailAPIView, CharityGuideByRegionAPIView
from charity_guide.models import CharityGuide
from rest_framework.test import APITestCase
from rest_framework import status
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
class CharityGuideAPITest(APITestCase):
    def setUp(self):
        # Published charity
        self.charity1 = CharityGuide.objects.create(
            name="Helping Hands",
            address="123 Yangon Road",
            region="Yangon",
            is_published=True,
            map_link="http://example.com/map",
            notes="Note 1",
            fb_page="http://facebook.com/helpinghands",
            detail={"mission": "Support local communities"}
        )

        # Unpublished charity (should not show up)
        self.charity2 = CharityGuide.objects.create(
            name="Hidden Hope",
            address="456 Mandalay Road",
            region="Mandalay",
            is_published=False,
            map_link="",
            notes="Note 2",
            fb_page="",
            detail={"mission": "Support youth"}
        )

        self.detail_url = reverse('charity-detail', args=[self.charity1.pk])
        self.list_url = reverse('charity-list')
        self.by_region_url = reverse('charity-by-region', args=["Yangon"])

    def test_list_published_charities(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        self.assertEqual(response.data['data'][0]['name'], "Helping Hands")

    def test_detail_view_published_charity(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['data']['name'], "Helping Hands")

    def test_detail_view_unpublished_charity_not_found(self):
        url = reverse('charity-detail', args=[self.charity2.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_charity_by_region(self):
        response = self.client.get(self.by_region_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)
        self.assertEqual(response.data['data'][0]['region'], "Yangon")

    def test_get_charity_by_region_empty(self):
        url = reverse('charity-by-region', args=["Mandalay"])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 0)
