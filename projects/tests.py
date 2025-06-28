from django.test import SimpleTestCase
from django.urls import reverse, resolve 
from projects.views import PopularProjectsAPIView, ProjectListAPIView, UpcomingProjectsAPIView, OngoingProjectsAPIView, PastProjectsAPIView ,ProjectDetailAPIView
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date, timedelta
from .models import Project, ProjectImage
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import tempfile
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

class ProjectAPITestCase(APITestCase):
    def setUp(self):
        # Helper image
        self.image = self.generate_test_image()

        # Projects
        self.upcoming = Project.objects.create(
            title="Upcoming Project",
            description="Upcoming",
            category="UPCOMING",
            start_date=date.today() + timedelta(days=30),
            is_published=True,
            views=10,
        )

        self.ongoing = Project.objects.create(
            title="Ongoing Project",
            description="Ongoing",
            category="ONGOING",
            start_date=date.today() - timedelta(days=5),
            is_published=True,
            views=50,
        )

        self.past = Project.objects.create(
            title="Past Project",
            description="Past",
            category="PAST",
            start_date=date.today() - timedelta(days=365),
            is_published=True,
            views=30,
        )

        self.unpublished = Project.objects.create(
            title="Hidden Project",
            description="Unpublished",
            category="UPCOMING",
            start_date=date.today() + timedelta(days=60),
            is_published=False,
            views=100,
        )

        # Add images to published projects
        for project in [self.upcoming, self.ongoing, self.past]:
            ProjectImage.objects.create(project=project, image=self.image)

    def generate_test_image(self):
        img = Image.new('RGB', (100, 100), color='blue')
        tmp_file = tempfile.NamedTemporaryFile(suffix='.png')
        img.save(tmp_file, 'PNG')
        tmp_file.seek(0)
        return SimpleUploadedFile(tmp_file.name, tmp_file.read(), content_type='image/png')

    def test_project_list(self):
        url = reverse('project-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "success")
        self.assertEqual(len(response.data["data"]), 3)  

    def test_popular_projects(self):
        url = reverse('popular-projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"][0]['title'], "Ongoing Project") 

    def test_upcoming_projects(self):
        url = reverse('upcoming-projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(all(p['category'] == "UPCOMING" for p in response.data["data"]))

    def test_ongoing_projects(self):
        url = reverse('ongoing-projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 1)
        self.assertEqual(response.data["data"][0]['title'], "Ongoing Project")

    def test_past_projects(self):
        url = reverse('past-projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 1)
        self.assertEqual(response.data["data"][0]['title'], "Past Project")

    def test_project_detail_success(self):
        url = reverse('project-detail', kwargs={"pk": self.past.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]["title"], "Past Project")

    def test_project_detail_not_found(self):
        url = reverse('project-detail', kwargs={"pk": 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["message"], "Project not found")
