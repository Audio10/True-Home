from django.db import models


class DateModel(models.Model):

    title = models.CharField(max_length=255)

    created_at = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the object was created.'
    )

    updated_at = models.DateTimeField(
        'updated at',
        auto_now=True,
        help_text='Date time on which the object was last modified.'
    )

    status = models.CharField(max_length=35, null=False)

    class Meta:
        """Meta option."""

        abstract = True

        get_latest_by = 'created_at'
        ordering = ['-created_at', '-updated_at']
