from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Twitter

class TwitterPlugin(CMSPluginBase):
    model = Twitter
    name = settings.TWITTER_PLUGIN_NAME
    module = settings.TWITTER_PLUGIN_MODULE_NAME
    render_template = "cmsplugin_twitter/plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
        })
        return context


plugin_pool.register_plugin(TwitterPlugin)
