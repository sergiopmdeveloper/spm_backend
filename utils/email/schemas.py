from ninja import Schema


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
