import pytest

from utils.email.email import EmailHandler
from utils.email.schemas import EmailIn


@pytest.fixture
def email_in() -> EmailIn:
    """
    Email in fixture

    Returns
    -------
    EmailIn
        The email in instance
    """

    return EmailIn(
        name="Name",
        email="Email",
        motivation="Motivation",
        message="Message",
    )


@pytest.fixture
def email_handler() -> EmailHandler:
    """
    Email handler fixture

    Returns
    -------
    EmailHandler
        The email handler instance
    """

    return EmailHandler()
