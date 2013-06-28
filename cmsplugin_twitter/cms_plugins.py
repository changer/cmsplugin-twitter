from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import Twitter

class TwitterPlugin(CMSPluginBase):
    model = Twitter
    name = _("Twitter feed")
    render_template = "cmsplugin_twitter/plugin.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
        })
        return context


plugin_pool.register_plugin(TwitterPlugin)
