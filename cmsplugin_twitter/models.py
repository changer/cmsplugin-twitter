from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _
from django.db import models


class Twitter(CMSPlugin):
    username = models.CharField(_('Twitter Handle'), max_length=75)
    widget_id = models.CharField('Widget Id', max_length=100)
    theme = models.CharField('Theme(dark or light)', max_length=5)
    height = models.CharField('Height in px)', max_length=4)
    width = models.CharField('Width in px)', max_length=4)
