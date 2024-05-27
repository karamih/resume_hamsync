from rest_framework import serializers
from .models import (ResumeModel, EducationModel, ProjectModel, SkillModel, ImportantLinkModel, WorkExModel)


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationModel
        fields = ['id', 'title', 'description', 'college_name', 'date_start', 'date_end']


class ProjectSerializer(serializers.ModelSerializer):
    resume = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProjectModel
        fields = ['id', 'title', 'description', 'url', 'date_start', 'date_end', 'resume']


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkillModel
        fields = ['id', 'name', 'rate']


class ImportantLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImportantLinkModel
        fields = ['id', 'name', 'url']


class WorkExSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExModel
        fields = ['id', 'title', 'description', 'company_name', 'date_start', 'date_end']


class ResumeSerializer(serializers.ModelSerializer):
    educations = EducationSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    links = ImportantLinkSerializer(many=True, read_only=True)
    experiences = WorkExSerializer(many=True, read_only=True)

    class Meta:
        model = ResumeModel
        fields = ['id', 'user', 'created_at', 'updated_at', 'educations', 'projects', 'skills', 'links', 'experiences']
