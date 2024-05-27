from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

User = get_user_model()


class ResumeModel(models.Model):
    user = models.OneToOneField(to=User, related_name='resumes', verbose_name=_('user'), on_delete=models.CASCADE)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'resumes'
        verbose_name = _('Resume')
        verbose_name_plural = _('Resumes')

    def __str__(self):
        return f'resume-{self.pk} --- user-{self.user}'


class EducationModel(models.Model):
    resume = models.ForeignKey(to=ResumeModel, related_name='educations', verbose_name=_('resume'),
                               on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), max_length=200, blank=True, null=True)
    college_name = models.CharField(verbose_name=_('college name'), max_length=50)
    date_start = models.DateField(verbose_name=_('date start'))
    date_end = models.DateField(verbose_name=_('date end'), null=True, blank=True)

    class Meta:
        db_table = 'educations'
        verbose_name = _('Education')
        verbose_name_plural = _('Educations')

    def __str__(self):
        return self.title


class ImportantLinkModel(models.Model):
    resume = models.ForeignKey(to=ResumeModel, related_name='links', verbose_name=_('resume'), on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('name'), max_length=50)
    url = models.URLField(verbose_name=_('url'), max_length=70)

    class Meta:
        db_table = 'important_links'
        verbose_name = _('Important Link')
        verbose_name_plural = _('Important Links')

    def __str__(self):
        return self.name


class SkillModel(models.Model):
    resume = models.ForeignKey(to=ResumeModel, related_name='skills', verbose_name=_('resume'),
                               on_delete=models.CASCADE)
    name = models.CharField(verbose_name=_('name'), max_length=50),
    rate = models.PositiveIntegerField(
        verbose_name=_('rate'),
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )

    class Meta:
        db_table = 'skills'
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')

    def __str__(self):
        return self.name


class ProjectModel(models.Model):
    resume = models.ForeignKey(to=ResumeModel, related_name='projects', verbose_name=_('resume'),
                               on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), max_length=200, blank=True, null=True)
    url = models.URLField(verbose_name=_('url'), max_length=70)
    date_start = models.DateField(verbose_name=_('date start'))
    date_end = models.DateField(verbose_name=_('date end'), null=True, blank=True)

    class Meta:
        db_table = 'projects'
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.title


class WorkExModel(models.Model):
    resume = models.ForeignKey(to=ResumeModel, related_name='experiences', verbose_name=_('resume'),
                               on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_('title'), max_length=50)
    description = models.TextField(verbose_name=_('description'), max_length=200, blank=True, null=True)
    company_name = models.CharField(verbose_name=_('company name'), max_length=50)
    date_start = models.DateField(verbose_name=_('date start'))
    date_end = models.DateField(verbose_name=_('date end'), null=True, blank=True)

    class Meta:
        db_table = 'work_experiences'
        verbose_name = _('Work Experience')
        verbose_name_plural = _('Work Experiences')

    def __str__(self):
        return self.title
