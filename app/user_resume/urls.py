from django.urls import path

from .views import (ProjectView, ProjectListView, SkillView, SkillListView,
                    ImportantLinkView, ImportantLinkListView, EducationView, EducationListView, WorkExView,
                    WorkExListView)

urlpatterns = [
    path('projects', ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>', ProjectView.as_view(), name='project-details'),

    path('skills', SkillListView.as_view(), name='skill-list'),
    path('skills/<int:pk>', SkillView.as_view(), name='skill-details'),

    path('links', ImportantLinkListView.as_view(), name='link-list'),
    path('links/<int:pk>', ImportantLinkView.as_view(), name='link-details'),

    path('educations', EducationListView.as_view(), name='education-list'),
    path('educations/<int:pk>', EducationView.as_view(), name='education-details'),

    path('experiences', WorkExListView.as_view(), name='experience-list'),
    path('experiences/<int:pk>', WorkExView.as_view(), name='experience-details')
]
