import os

import resend
from dotenv import load_dotenv

from utils.email.other import EMAIL_TEMPLATE
from utils.email.schemas import EmailIn, EmailResponse

load_dotenv()


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
            "subject": f"SPM: {email.motivation}",
            "html": EMAIL_TEMPLATE.format(email=email.email, message=email.message),
        }

        email_sent = resend.Emails.send(params)

        return EmailResponse(email_id=email_sent["id"])
