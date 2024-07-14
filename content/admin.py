from django.contrib import admin

from .models import Job, Project, Study


@admin.register(Study)
class StudyAdmin(admin.ModelAdmin):
    """
    Study admin
    """

    list_display = (
        "name",
        "school",
        "description",
        "start_date",
        "end_date",
        "created_at",
        "updated_at",
    )


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    """
    Job admin
    """

    list_display = (
        "name",
        "company",
        "description",
        "start_date",
        "end_date",
        "created_at",
        "updated_at",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    """
    Project admin
    """

    list_display = ("name", "description", "technologies", "link")
