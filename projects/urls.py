from django.urls import path
from .views import ProjectListAPIView, ProjectDetailAPIView, PopularProjectsAPIView, UpcomingProjectsAPIView, OngoingProjectsAPIView, PastProjectsAPIView

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('projects/popular/', PopularProjectsAPIView.as_view(), name='popular-projects'),
    path('projects/upcoming/', UpcomingProjectsAPIView.as_view(), name='upcoming-projects'),
    path('projects/ongoing/', OngoingProjectsAPIView.as_view(), name='ongoing-projects'),
    path('projects/past/', PastProjectsAPIView.as_view(), name='past-projects'),
]
