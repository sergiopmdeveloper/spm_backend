import os

import resend
from dotenv import load_dotenv

load_dotenv()


class EmailHandler:
    """
    Email handler
    """

    API_KEY = os.environ.get("RESEND_API_KEY")

    def send_email(self) -> resend.Email:
        """
        TODO - To be implemented...
        """

        resend.api_key = self.API_KEY

        params: resend.Emails.SendParams = {
            "from": "Sergio <sergio.pm.developer@gmail.com>",
            "to": ["sergio.pm.developer@gmail.com"],
            "subject": "Development",
            "html": "<strong>Implementation works!</strong>",
        }

        email = resend.Emails.send(params)

        return email
