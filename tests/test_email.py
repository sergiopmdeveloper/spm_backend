from unittest.mock import patch

from utils.email.email import EmailHandler
from utils.email.schemas import EmailIn


def test_send_email_calls_resend_emails_send(
    email_in: EmailIn, email_handler: EmailHandler
):
    """
    Test that the send_email method of the EmailHandler
    class calls the Resend.Emails.send method
    """

    with patch("resend.Emails.send") as mock_send:
        mock_send.return_value = {"id": "1234"}
        email_handler.send_email(email=email_in)

    mock_send.assert_called_once()


def test_send_email_response(email_in: EmailIn, email_handler: EmailHandler):
    """
    Test that the send_email method of the EmailHandler
    class returns the expected response
    """

    with patch("resend.Emails.send") as mock_send:
        mock_send.return_value = {"id": "1234"}
        response = email_handler.send_email(email=email_in)

    assert response.email_id == "1234"
