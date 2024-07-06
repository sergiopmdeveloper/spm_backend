from django.contrib import admin

from .models import Study


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
