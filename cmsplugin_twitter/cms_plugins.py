from cmss.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from models import Twitter


class TwitterPlugin(CMSPluginBase):
    model = Twitter
    name = _("Django CMS Twitter")
    render_template = "cms_plugins/twitter.html"

    def render(self, context, instance, placeholder):
        context.update({
            'object': instance,
            })
        return context

plugin_pool.register_plugin(TwitterPlugin)
