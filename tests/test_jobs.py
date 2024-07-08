import pytest
from django.core.exceptions import ValidationError

from content.models import Job
from tests.constants import client


def test_job_dates_validation():
    """
    Test that ValidationError exception is raised
    when a job is created with an end date
    that is prior to the start date
    """

    job = Job(
        name="Job 1",
        company="Company 1",
        description="Description 1",
        start_date="2024-02-01",
        end_date="2024-01-01",
    )

    with pytest.raises(ValidationError) as exc_info:
        job.save()

    assert (
        exc_info.value.messages[0]
        == "End date must be equal or greater than start date"
    )


@pytest.mark.django_db
def test_get_jobs():
    """
    Test that the GET method on
    /api/jobs returns all jobs
    """

    jobs_to_create = [
        {
            "name": "Job 1",
            "company": "Company 1",
            "description": "Description 1",
            "start_date": "2024-01-01",
            "end_date": "2024-01-01",
        },
        {
            "name": "Job 2",
            "company": "Company 2",
            "description": "Description 2",
            "start_date": "2024-02-01",
            "end_date": None,
        },
    ]

    Job.objects.bulk_create([Job(**job) for job in jobs_to_create])

    response = client.get("/jobs")

    assert response.status_code == 200
    assert response.json() == jobs_to_create
