from datetime import date
from typing import Optional

from ninja import Schema


class StudyOut(Schema):
    """
    Study out schema
    """

    name: str
    school: str
    description: str
    start_date: date
    end_date: Optional[date] = None
