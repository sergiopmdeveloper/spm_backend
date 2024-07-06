from django.core.handlers.wsgi import WSGIRequest
from ninja import NinjaAPI

api = NinjaAPI()


@api.get("/studies", response=list)
def get_studies(request: WSGIRequest):
    """
    Get studies

    Parameters
    ----------
    request : WSGIRequest
        The request object, not used
    """

    return []
