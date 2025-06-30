from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.urls import reverse
from .models import Project
from .serializers import ProjectSerializer

class PopularProjectsAPIView(APIView):
    def get(self, request):
        projects = Project.objects.prefetch_related('images').filter(is_published=True).order_by('-views')[:10]
        serializer = ProjectSerializer(projects, many=True)
        return Response({
            "meta": {
                "message": "Popular projects retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "self": request.build_absolute_uri(),
            }
        }, status=status.HTTP_200_OK)


class ProjectListAPIView(APIView):
    def get(self, request):
        projects = Project.objects.prefetch_related('images').filter(is_published=True)
        serializer = ProjectSerializer(projects, many=True)
        return Response({
            "meta": {
                "message": "Project list retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "self": request.build_absolute_uri(),
            }
        }, status=status.HTTP_200_OK)


class RadioProjectsAPIView(APIView):
    def get(self, request):
        projects = Project.objects.prefetch_related('images').filter(
            is_published=True,
            category="RADIO"
        ).order_by('-start_date')
        serializer = ProjectSerializer(projects, many=True)
        return Response({
            "meta": {
                "message": "Radion program projects retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "self": request.build_absolute_uri(),
            }
        }, status=status.HTTP_200_OK)


class StreetProjectsAPIView(APIView):
    def get(self, request):
        projects = Project.objects.prefetch_related('images').filter(
            is_published=True,
            category="STREET"
        ).order_by('-start_date')
        serializer = ProjectSerializer(projects, many=True)
        return Response({
            "meta": {
                "message": "Street projects retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "self": request.build_absolute_uri(),
            }
        }, status=status.HTTP_200_OK)

class MonthlyProjectsAPIView(APIView):
    def get(self, request):
        projects = Project.objects.prefetch_related('images').filter(
            is_published=True,
            category="MONTHLY"
        ).order_by('-start_date')
        serializer = ProjectSerializer(projects, many=True)
        return Response({
            "meta": {
                "message": "Monthly projects retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "self": request.build_absolute_uri(),
            }
        }, status=status.HTTP_200_OK)

class CrisisProjectsAPIView(APIView):
    def get(self, request):
        projects = Project.objects.prefetch_related('images').filter(
            is_published=True,
            category="CRISIS"
        ).order_by('-start_date')
        serializer = ProjectSerializer(projects, many=True)
        return Response({
            "meta": {
                "message": "Crisis projects retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "self": request.build_absolute_uri(),
            }
        }, status=status.HTTP_200_OK)

class ProjectDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            project = Project.objects.prefetch_related('images').get(pk=pk, is_published=True)
        except Project.DoesNotExist:
            return Response({
                "meta": {
                    "message": "Project not found",
                    "status_code": status.HTTP_404_NOT_FOUND
                },
                "data": None,
                "links": {
                    "self": request.build_absolute_uri(),
                }
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(project)
        return Response({
            "meta": {
                "message": "Project detail retrieved successfully",
                "status_code": status.HTTP_200_OK
            },
            "data": serializer.data,
            "links": {
                "self": request.build_absolute_uri(),
            }
        }, status=status.HTTP_200_OK)
