from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class Twitter(CMSPlugin):
    THEME_CHOICES = (
        ('light', _('Light')),
        ('dark', _('Dark')),
    )

    username = models.CharField(_('Twitter handle'), max_length=75)
    widget_id = models.CharField(_('Widget id'), max_length=100, help_text=_(
        'Create a widget at <a href="https://twitter.com/settings/widgets" '
        'target="_blank">https://twitter.com/settings/widgets</a> and '
        'copy/paste the id of the widget into this field.')
    )
    theme = models.CharField(_('Theme'), max_length=5, choices=THEME_CHOICES)
    width = models.CharField(_('Width in pixels'), max_length=4)
    height = models.CharField(_('Height in pixels'), max_length=4)
