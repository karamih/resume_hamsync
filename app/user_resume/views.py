from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView

from .serializer import (ResumeSerializer, ProjectSerializer, SkillSerializer, ImportantLinkSerializer,
                         EducationSerializer, WorkExSerializer
                         )
from .models import (ResumeModel, ProjectModel, SkillModel, ImportantLinkModel, EducationModel, WorkExModel)


class ResumeView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ResumeSerializer

    def get_object(self):
        return ResumeModel.objects.get(user=self.request.user)


class ProjectListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return ProjectModel.objects.filter(resume__user=self.request.user)

    def perform_create(self, serializer):
        resume = ResumeModel.objects.get(user=self.request.user)
        serializer.save(resume=resume)


class ProjectView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer

    def get_queryset(self):
        return ProjectModel.objects.filter(resume__user=self.request.user)


class SkillListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillSerializer

    def get_queryset(self):
        return SkillModel.objects.filter(resume__user=self.request.user)

    def perform_create(self, serializer):
        resume = ResumeModel.objects.get(user=self.request.user)
        serializer.save(resume=resume)


class SkillView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = SkillSerializer

    def get_queryset(self):
        return SkillModel.objects.filter(resume__user=self.request.user)


class ImportantLinkListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImportantLinkSerializer

    def get_queryset(self):
        return ImportantLinkModel.objects.filter(resume__user=self.request.user)

    def perform_create(self, serializer):
        resume = ResumeModel.objects.get(user=self.request.user)
        serializer.save(resume=resume)


class ImportantLinkView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ImportantLinkSerializer

    def get_queryset(self):
        return ImportantLinkModel.objects.filter(resume__user=self.request.user)


class EducationListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EducationSerializer

    def get_queryset(self):
        return EducationModel.objects.filter(resume__user=self.request.user)

    def perform_create(self, serializer):
        resume = ResumeModel.objects.get(user=self.request.user)
        serializer.save(resume=resume)


class EducationView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = EducationSerializer

    def get_queryset(self):
        return EducationModel.objects.filter(resume__user=self.request.user)


class WorkExListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkExSerializer

    def get_queryset(self):
        return WorkExModel.objects.filter(resume__user=self.request.user)

    def perform_create(self, serializer):
        resume = ResumeModel.objects.get(user=self.request.user)
        serializer.save(resume=resume)


class WorkExView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkExSerializer

    def get_queryset(self):
        return WorkExModel.objects.filter(resume__user=self.request.user)
