import os

import resend
from dotenv import load_dotenv
from ninja import Schema

load_dotenv()


class EmailIn(Schema):
    """
    Email in schema
    """

    name: str
    email: str
    motivation: str
    message: str


class EmailResponse(Schema):
    """
    Email response schema
    """

    email_id: str


class EmailHandler:
    """
    Email handler
    """

    API_KEY = os.environ.get("RESEND_API_KEY")

    def send_email(self, email: EmailIn) -> EmailResponse:
        """
        Send email

        Parameters
        ----------
        email : EmailIn
            The email object

        Returns
        -------
        EmailResponse
            The email response
        """

        resend.api_key = self.API_KEY

        params: resend.Emails.SendParams = {
            "from": "SPM <onboarding@resend.dev>",
            "to": ["sergio.pm.developer@gmail.com"],
            "subject": email.motivation,
            "html": f"""
                <div>
                    <h1>{email.email}</h1>
                    <p>{email.message}</p>
                </div>
            """,
        }

        email_sent = resend.Emails.send(params)

        return EmailResponse(email_id=email_sent["id"])
