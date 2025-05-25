from django.urls import path
from .views import CharityGuideListAPIView, CharityGuideDetailAPIView, CharityGuideByRegionAPIView

urlpatterns = [
    path('charities/', CharityGuideListAPIView.as_view(), name='charity-list'),
    path('charities/<int:pk>/', CharityGuideDetailAPIView.as_view(), name='charity-detail'),
    path('charities/region/<str:region_name>/', CharityGuideByRegionAPIView.as_view(), name='charity-by-region'),
]
