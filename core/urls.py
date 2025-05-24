from django.urls import path
from .views import PartnerOrganizationListAPIView

urlpatterns = [
    path('platforms/', PartnerOrganizationListAPIView.as_view(), name='social-platforms-list'),
    path('partners/', PartnerOrganizationListAPIView.as_view(), name='partner-orgs-list'),
]
  