from django.core.exceptions import ValidationError
from django.db import models


class Study(models.Model):
    """
    Study model
    """

    name = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Metadata options
        """

        db_table = "studies"
        verbose_name_plural = "Studies"

    def _validate_fields(self) -> None:
        """
        Validates the fields of the model

        Raises
        ------
        ValidationError
            If there are any validation errors
        """

        errors = {}

        if self.end_date and self.end_date < self.start_date:
            errors["end_date"] = "End date must be equal or greater than start date"

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs) -> None:
        """
        Custom save method
        """

        self._validate_fields()

        super().save(*args, **kwargs)


class Job(models.Model):
    """
    Job model
    """

    name = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        """
        Metadata options
        """

        db_table = "jobs"
        verbose_name_plural = "Jobs"

    def _validate_fields(self) -> None:
        """
        Validates the fields of the model

        Raises
        ------
        ValidationError
            If there are any validation errors
        """

        errors = {}

        if self.end_date and self.end_date < self.start_date:
            errors["end_date"] = "End date must be equal or greater than start date"

        if errors:
            raise ValidationError(errors)

    def save(self, *args, **kwargs) -> None:
        """
        Custom save method
        """

        self._validate_fields()

        super().save(*args, **kwargs)


class Project(models.Model):
    """
    Project model
    """

    name = models.CharField(max_length=255)
    description = models.TextField()
    technologies = models.CharField(max_length=255)
    link = models.URLField()

    class Meta:
        """
        Metadata options
        """

        db_table = "projects"
        verbose_name_plural = "Projects"
