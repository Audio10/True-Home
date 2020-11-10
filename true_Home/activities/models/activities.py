"""Activity model."""

from django.db import models
from utils.models import DateModel
from activities.models.properties import Property


class Activity(DateModel):
    """Activity model"""
    property = models.ForeignKey(Property, on_delete=models.CASCADE, null=False)

    schedule = models.DateTimeField(
        'schedule',
        null=False,
        help_text='Date time on which the activity is scheduled.'
    )

    def __str__(self):
        """Return the activity name."""
        return self.title
