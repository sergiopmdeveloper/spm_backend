from django.core.handlers.wsgi import WSGIRequest
from ninja import NinjaAPI

from content.models import Study
from content.schemas import StudyOut

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
