from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from contact.views import ContactMessageView

class TestUrls(SimpleTestCase):
    def test_contact_list_url_is_resolved(self):
        url = reverse('contact')
        self.assertEqual(resolve(url).func.view_class, ContactMessageView)

