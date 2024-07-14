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


class JobOut(Schema):
    """
    Job out schema
    """

    name: str
    company: str
    description: str
    start_date: date
    end_date: Optional[date] = None


class ProjectOut(Schema):
    """
    Project out schema
    """

    name: str
    description: str
    technologies: str
    link: str
