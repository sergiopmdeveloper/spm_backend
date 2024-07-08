from django.core.handlers.wsgi import WSGIRequest
from ninja import NinjaAPI

from content.models import Job, Study
from content.schemas import JobOut, StudyOut

api = NinjaAPI()


@api.get("/studies", response=list[StudyOut])
def get_studies(request: WSGIRequest):
    """
    Get studies

    Parameters
    ----------
    request : WSGIRequest
        The request object, not used
    """

    return Study.objects.all()


@api.get("/jobs", response=list[JobOut])
def get_jobs(request: WSGIRequest):
    """
    Get jobs

    Parameters
    ----------
    request : WSGIRequest
        The request object, not used
    """

    return Job.objects.all()
