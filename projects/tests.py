from django.test import SimpleTestCase
from django.urls import reverse, resolve
from rest_framework.test import APITestCase
from rest_framework import status
from datetime import date, timedelta
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image
import tempfile

from projects.views import (
    ProjectListAPIView, ProjectDetailAPIView, PopularProjectsAPIView,
    RadioProjectsAPIView, StreetProjectsAPIView, MonthlyProjectsAPIView,
    CrisisProjectsAPIView
)
from .models import Project, ProjectImage


class TestUrls(SimpleTestCase):
    def test_pj_list_url_is_resolved(self):
        url = reverse('project-list')
        self.assertEqual(resolve(url).func.view_class, ProjectListAPIView)

    def test_pj_detail_url_is_resolved(self):
        url = reverse('project-detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, ProjectDetailAPIView)

    def test_popular_pj_url_is_resolved(self):
        url = reverse('popular-projects')
        self.assertEqual(resolve(url).func.view_class, PopularProjectsAPIView)

    def test_radio_pj_url_is_resolved(self):
        url = reverse('radio-projects')
        self.assertEqual(resolve(url).func.view_class, RadioProjectsAPIView)

    def test_street_pj_url_is_resolved(self):
        url = reverse('street-projects')
        self.assertEqual(resolve(url).func.view_class, StreetProjectsAPIView)

    def test_monthly_pj_url_is_resolved(self):
        url = reverse('monthly-projects')
        self.assertEqual(resolve(url).func.view_class, MonthlyProjectsAPIView)

    def test_crisis_pj_url_is_resolved(self):
        url = reverse('crisis-projects')
        self.assertEqual(resolve(url).func.view_class, CrisisProjectsAPIView)


class ProjectAPITestCase(APITestCase):
    def setUp(self):
        self.image = self.generate_test_image()

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

        self.radio = Project.objects.create(
            title="Radio Project",
            description="Radio",
            category="RADIO",
            start_date=date.today() - timedelta(days=20),
            is_published=True,
            views=25,
        )

        self.street = Project.objects.create(
            title="Street Project",
            description="Street",
            category="STREET",
            start_date=date.today() - timedelta(days=10),
            is_published=True,
            views=40,
        )

        self.monthly = Project.objects.create(
            title="Monthly Project",
            description="Monthly",
            category="MONTHLY",
            start_date=date.today() - timedelta(days=15),
            is_published=True,
            views=35,
        )

        self.crisis = Project.objects.create(
            title="Crisis Project",
            description="Crisis",
            category="CRISIS",
            start_date=date.today() - timedelta(days=7),
            is_published=True,
            views=20,
        )

        self.unpublished = Project.objects.create(
            title="Hidden Project",
            description="Unpublished",
            category="UPCOMING",
            start_date=date.today() + timedelta(days=60),
            is_published=False,
            views=100,
        )

        for project in Project.objects.filter(is_published=True):
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
        self.assertEqual(response.data["meta"]["status_code"], 200)
        self.assertEqual(len(response.data["data"]), 6)

    def test_popular_projects(self):
        url = reverse('popular-projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"][0]['title'], "Ongoing Project")  # views=50

    def test_radio_projects(self):
        url = reverse('radio-projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 1)
        self.assertEqual(response.data["data"][0]['title'], "Radio Project")

    def test_street_projects(self):
        url = reverse('street-projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 1)
        self.assertEqual(response.data["data"][0]['title'], "Street Project")

    def test_monthly_projects(self):
        url = reverse('monthly-projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 1)
        self.assertEqual(response.data["data"][0]['title'], "Monthly Project")

    def test_crisis_projects(self):
        url = reverse('crisis-projects')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data["data"]), 1)
        self.assertEqual(response.data["data"][0]['title'], "Crisis Project")

    def test_project_detail_success(self):
        url = reverse('project-detail', kwargs={"pk": self.monthly.pk})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["data"]["title"], "Monthly Project")

    def test_project_detail_not_found(self):
        url = reverse('project-detail', kwargs={"pk": 999})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data["meta"]["message"], "Project not found")
