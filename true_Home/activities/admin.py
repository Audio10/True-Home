"""Circles admin."""
from django.contrib import admin
from activities.models import Property
from activities.models import Activity
from activities.models import Survey

admin.site.site_header = 'True Home'
admin.site.index_title = 'True Home Admin'
admin.site.site_title = "True Home Admin"


@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    """Property admin."""

    list_display = (
        'id',
        'title',
        'address',
        'description',
        'created_at',
        'updated_at',
        'disabled_at',
        'status'
    )

    search_fields = ('title', 'status')


@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    """Activity admin."""

    list_display = (
        'id',
        'property_id',
        'title',
        'schedule',
        'created_at',
        'updated_at',
        'status'
    )

    search_fields = ('title', 'status')


@admin.register(Survey)
class ActivityAdmin(admin.ModelAdmin):
    """Activity admin."""

    list_display = (
        'id',
        'answers',
        'created_at',
        'activity'
    )

    search_fields = ('activity',)

