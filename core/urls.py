from django.urls import path
from .views import PartnerOrganizationListAPIView

urlpatterns = [
    path('partners/', PartnerOrganizationListAPIView.as_view(), name='partner-list'),
]
