from django.core.handlers.wsgi import WSGIRequest
from ninja import NinjaAPI

from content.models import Job, Project, Study
from content.schemas import JobOut, ProjectOut, StudyOut
from utils.email import EmailHandler

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


@api.get("/projects", response=list[ProjectOut])
def get_projects(request: WSGIRequest):
    """
    Get projects

    Parameters
    ----------
    request : WSGIRequest
        The request object, not used
    """

    return Project.objects.all()


@api.post("/email")
def send_email(request: WSGIRequest):
    """
    Send email

    Parameters
    ----------
    request : WSGIRequest
        The request object, not used
    """

    email_handler = EmailHandler()

    sent_email = email_handler.send_email()

    return sent_email
