from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from core.views import SocialPlatformListAPIView, PartnerOrganizationListAPIView,  ActivityPhotoListAPIView, terms_view, DonationCertificateListAPIView
from core.models import SocialPlatform, PartnerOrganization, ActivityPhoto, DonationCertificate
from rest_framework.test import APITestCase
from rest_framework import status
from django.core.files.uploadedfile import SimpleUploadedFile
import tempfile
from PIL import Image
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
    
    def test_certificate_list_url_is_resolved(self):
        url = reverse('certificates-list')
        self.assertEqual(resolve(url).func.view_class, DonationCertificateListAPIView)
class TestAPIViews(APITestCase):
    def setUp(self):
        # SocialPlatform setup
        self.social1 = SocialPlatform.objects.create(
            platform_name="Facebook", url="https://facebook.com"
        )
        self.social2 = SocialPlatform.objects.create(
            platform_name="Twitter", url="https://twitter.com"
        )

        # PartnerOrganization setup
        self.partner1 = PartnerOrganization.objects.create(
            org_name="Partner 1", website="https://partner1.com", description="Desc 1"
        )
        self.partner2 = PartnerOrganization.objects.create(org_name="Partner 2")

        # ActivityPhoto setup
        image2 = self.create_test_image()
        self.photo1 = ActivityPhoto.objects.create(image=image2, caption="Caption 1")
        self.photo2 = ActivityPhoto.objects.create(image=image2, caption="Caption 2")
        self.photo3 = ActivityPhoto.objects.create(image=image2) 
        
        self.cert_file = SimpleUploadedFile("cert.pdf", b"fake-pdf-content", content_type="application/pdf")
        self.cert = DonationCertificate.objects.create(
             certificate_file=self.cert_file
        )


    def create_test_image(self):
        # Create a simple image for testing ImageField
        img = Image.new('RGB', (100, 100), color='red')
        tmp_file = tempfile.NamedTemporaryFile(suffix='.png')
        img.save(tmp_file)
        tmp_file.seek(0)
        return SimpleUploadedFile(tmp_file.name, tmp_file.read(), content_type='image/png')

    def test_socialplatform_list_api(self):
        url = reverse('social-platforms-list') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 2)
        self.assertIn('platform_name', response.data['data'][0])

    def test_partnerorganization_list_api(self):
        url = reverse('partner-orgs-list') 
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 2)
        self.assertIn('org_name', response.data['data'][0])

    def test_activityphoto_list_api(self):
        url = reverse('activity-photo-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 3)

        captions = [item['caption'] for item in response.data['data']]
        self.assertIn("Caption 1", captions)
        self.assertIn("Caption 2", captions)
        self.assertIn(self.photo3.caption, captions)  


    def test_certificate_list_api(self):
        url = reverse('certificates-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['data']), 1)

