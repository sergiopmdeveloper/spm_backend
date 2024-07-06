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
