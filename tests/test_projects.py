import pytest

from content.models import Project
from tests.constants import client


@pytest.mark.django_db
def test_get_projects():
    """
    Test that the GET method on
    /api/projects returns all projects
    """

    projects_to_create = [
        {
            "name": "Project 1",
            "description": "Description 1",
            "technologies": "React,TypeScript",
            "link": "https://www.project1.com",
        },
        {
            "name": "Project 2",
            "description": "Description 2",
            "technologies": "Django,Alpine",
            "link": "https://www.project2.com",
        },
    ]

    Project.objects.bulk_create([Project(**project) for project in projects_to_create])

    response = client.get("/projects")

    assert response.status_code == 200
    assert response.json() == projects_to_create
