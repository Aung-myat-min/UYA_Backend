from django.urls import path
from .views import ProjectListAPIView, ProjectDetailAPIView, PopularProjectsAPIView, RadioProjectsAPIView, StreetProjectsAPIView, MonthlyProjectsAPIView, CrisisProjectsAPIView

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('projects/popular/', PopularProjectsAPIView.as_view(), name='popular-projects'),
    path('projects/radio/', RadioProjectsAPIView.as_view(), name='radio-projects'),
    path('projects/street/', StreetProjectsAPIView.as_view(), name='street-projects'),
    path('projects/monthly/', MonthlyProjectsAPIView.as_view(), name='monthly-projects'),
    path('projects/crisis/', CrisisProjectsAPIView.as_view(), name='crisis-projects'),
]
