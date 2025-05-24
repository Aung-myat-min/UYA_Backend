from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Project
from .serializers import ProjectSerializer

class ProjectListAPIView(APIView):
    def get(self, request):
        projects = Project.objects.prefetch_related('images').filter(is_published=True)
        serializer = ProjectSerializer(projects, many=True)
        return Response({
            "status": "success",
            "message": "Project list retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


class ProjectDetailAPIView(APIView):
    def get(self, request, pk):
        try:
            project = Project.objects.prefetch_related('images').get(pk=pk, is_published=True)
        except Project.DoesNotExist:
            return Response({
                "status": "error",
                "message": "Project not found",
                "data": None
            }, status=status.HTTP_404_NOT_FOUND)

        serializer = ProjectSerializer(project)
        return Response({
            "status": "success",
            "message": "Project detail retrieved successfully",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
