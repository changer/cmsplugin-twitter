from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from models import twitter

class TwitterPlugin(CMSPluginBase):
    model = Fb
    name = _("Django CMS Twitter")
    render_template = "cms_plugins/twitter.html"

    def render(self, context, instance, placeholder):
        context.update({
          'object': instance,
          })
        return context

plugin_pool.register_plugin(TwitterPlugin)
