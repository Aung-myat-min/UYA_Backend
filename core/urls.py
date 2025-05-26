from django.urls import path
from .views import SocialPlatformListAPIView,PartnerOrganizationListAPIView, ActivityPhotoListAPIView,terms_of_service

urlpatterns = [
    path("terms/", terms_of_service, name="terms_of_service"),
    path('platforms/', SocialPlatformListAPIView.as_view(), name='social-platforms-list'),
    path('partners/', PartnerOrganizationListAPIView.as_view(), name='partner-orgs-list'),
    path('activities/',ActivityPhotoListAPIView.as_view(),name='activity-photo-list')
]
  