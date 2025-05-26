from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from core.views import SocialPlatformListAPIView, PartnerOrganizationListAPIView,  ActivityPhotoListAPIView, terms_view

class TestUrls(SimpleTestCase):
    def test_platform_list_url_is_resolved(self):
        url = reverse('social-platforms-list')
        self.assertEqual(resolve(url).func.view_class, SocialPlatformListAPIView)

    def test_partner_list_url_is_resolved(self):
        url = reverse('partner-orgs-list')
        self.assertEqual(resolve(url).func.view_class, PartnerOrganizationListAPIView)

    def test_activity_list_url_is_resolved(self):
        url = reverse('activity-photo-list')
        self.assertEqual(resolve(url).func.view_class, ActivityPhotoListAPIView)
    
    def test_terms_url_is_resolved(self):
        url = reverse('terms_of_service')
        self.assertEqual(resolve(url).func, terms_view)


