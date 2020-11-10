"""Survey model."""

from django.db import models
from django.contrib.postgres.fields import JSONField
from activities.models.activities import Activity


class Survey(models.Model):
    """Survey model."""

    activity = models.OneToOneField(Activity, on_delete=models.SET_NULL, null=True)

    answers = JSONField()

    created_at = models.DateTimeField(
        'created at',
        null=False,
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )
