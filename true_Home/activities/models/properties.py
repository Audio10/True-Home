"""Property model."""

from django.db import models
from utils.models import DateModel


class Property(DateModel):
    """Property model"""

    address = models.CharField(null=False, max_length=255)
    description = models.TextField(blank=True, max_length=255)
    disabled_at = models.DateTimeField(
        'disabled at',
        blank=True,
        null=True,
        help_text='Date time on which the activity was disabled.'
    )

    def __str__(self):
        """Return the activity name."""
        return self.title
