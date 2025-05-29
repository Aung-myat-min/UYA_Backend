from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from contact.views import ContactMessageView
from contact.models import ContactMessage
from rest_framework.test import APITestCase
from unittest.mock import patch

class TestUrls(SimpleTestCase):
    def test_contact_list_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func.view_class, ContactMessageView)

class TestContactMessageView(APITestCase):
    def setUp(self):
        self.url = reverse('contact')
        self.valid_data = {
            'sender': "Htet Arkar",
            'email': "htetarkarlevi@gmail.com",
            'ph_number': "09791444137",
            'subject': "Testing",
            'message': "I'm testing.",
        }

    @patch('contact.views.send_mail')
    def test_valid_contact_message_POST_with_email_mock(self, mock_send_mail):
        response = self.client.post(self.url, data=self.valid_data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(ContactMessage.objects.count(), 1)
        self.assertEqual(ContactMessage.objects.first().email, "htetarkarlevi@gmail.com")
        self.assertEqual(mock_send_mail.call_count, 2)

    def test_invalid_contact_message_POST(self):
        response = self.client.post(self.url, data={}, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(ContactMessage.objects.count(), 0)
