# Generated by Django 4.2 on 2024-05-24 18:03

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("user_resume", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="skillmodel", name="name",),
        migrations.AlterField(
            model_name="educationmodel",
            name="date_end",
            field=models.DateField(blank=True, null=True, verbose_name="date end"),
        ),
        migrations.AlterField(
            model_name="educationmodel",
            name="date_start",
            field=models.DateField(verbose_name="date start"),
        ),
        migrations.AlterField(
            model_name="projectmodel",
            name="date_end",
            field=models.DateField(blank=True, null=True, verbose_name="date end"),
        ),
        migrations.AlterField(
            model_name="projectmodel",
            name="date_start",
            field=models.DateField(verbose_name="date start"),
        ),
        migrations.AlterField(
            model_name="resumemodel",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="resumes",
                to=settings.AUTH_USER_MODEL,
                verbose_name="user",
            ),
        ),
        migrations.AlterField(
            model_name="skillmodel",
            name="rate",
            field=models.PositiveIntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(5),
                ],
                verbose_name="rate",
            ),
        ),
        migrations.AlterField(
            model_name="workexmodel",
            name="date_end",
            field=models.DateField(blank=True, null=True, verbose_name="date end"),
        ),
        migrations.AlterField(
            model_name="workexmodel",
            name="date_start",
            field=models.DateField(verbose_name="date start"),
        ),
    ]
