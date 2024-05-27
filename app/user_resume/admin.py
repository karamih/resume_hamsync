from django.contrib import admin

from .models import (ResumeModel, ProjectModel, WorkExModel, SkillModel, ImportantLinkModel, EducationModel)


class ProjectAdmin(admin.StackedInline):
    model = ProjectModel
    fields = ['title', 'description', 'url', 'date_start', 'date_end']
    extra = 0


class WorkExAdmin(admin.StackedInline):
    model = WorkExModel
    fields = ['title', 'description', 'company_name', 'date_start', 'date_end']
    extra = 0


class SkillAdmin(admin.StackedInline):
    model = SkillModel
    fields = ['name', 'rate']
    extra = 0


class ImportantLinkAdmin(admin.StackedInline):
    model = ImportantLinkModel
    fields = ['name', 'url']
    extra = 0


class EducationAdmin(admin.StackedInline):
    model = EducationModel
    fields = ['title', 'description', 'college_name', 'date_start', 'date_end']
    extra = 0


@admin.register(ResumeModel)
class ResumeModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'created_time', 'updated_time']
    readonly_fields = ['created_time', 'updated_time']
    search_fields = ['id']
    list_filter = ['created_time', 'updated_time']

    inlines = [ProjectAdmin, WorkExAdmin, SkillAdmin, ImportantLinkAdmin, EducationAdmin]
