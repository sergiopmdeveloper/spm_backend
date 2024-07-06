import pytest
from django.core.exceptions import ValidationError
from ninja.testing import TestClient

from content.models import Study


def test_study_dates_validation():
    """
    Test that ValidationError exception is raised
    when a study is created with an end date
    that is prior to the start date
    """

    study = Study(
        name="Study 1",
        school="School 1",
        description="Description 1",
        start_date="2024-02-01",
        end_date="2024-01-01",
    )

    with pytest.raises(ValidationError) as exc_info:
        study.save()


@pytest.mark.django_db
def test_get_studies(client: TestClient):
    """
    Test that the GET method on
    /api/studies returns all studies
    """

    studies_to_create = [
        {
            "name": "Study 1",
            "school": "School 1",
            "description": "Description 1",
            "start_date": "2024-01-01",
            "end_date": "2024-01-01",
        },
        {
            "name": "Study 2",
            "school": "School 2",
            "description": "Description 2",
            "start_date": "2024-02-01",
            "end_date": None,
        },
    ]

    Study.objects.bulk_create([Study(**study) for study in studies_to_create])

    response = client.get("/studies")

    assert response.status_code == 200
    assert response.json() == studies_to_create
