from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from projects.views import PopularProjectsAPIView, ProjectListAPIView, UpcomingProjectsAPIView, OngoingProjectsAPIView, PastProjectsAPIView ,ProjectDetailAPIView

class TestUrls(SimpleTestCase):
    def test_pj_list_url_is_resolved(self):
        url = reverse('project-list')
        self.assertEqual(resolve(url).func.view_class, ProjectListAPIView)

    def test_pj_detail_list_url_is_resolved(self):
        url = reverse('project-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProjectDetailAPIView)
        
    def test_popular_pj_list_url_is_resolved(self):
        url = reverse('popular-projects')
        self.assertEqual(resolve(url).func.view_class, PopularProjectsAPIView)
        
    def test_upcoming_pj_list_url_is_resolved(self):
        url = reverse('upcoming-projects')
        self.assertEqual(resolve(url).func.view_class, UpcomingProjectsAPIView)
        
    def test_ongoing_pj_list_url_is_resolved(self):
        url = reverse('ongoing-projects')
        self.assertEqual(resolve(url).func.view_class, OngoingProjectsAPIView)
    
    def test_past_pj_list_url_is_resolved(self):
        url = reverse('past-projects')
        self.assertEqual(resolve(url).func.view_class, PastProjectsAPIView)




