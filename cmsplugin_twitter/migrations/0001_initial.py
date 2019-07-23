# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from __future__ import absolute_import
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20160404_1908'),
    ]

    operations = [
        migrations.CreateModel(
            name='Twitter',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('username', models.CharField(max_length=75, verbose_name='Twitter handle')),
                ('widget_id', models.CharField(help_text='Create a widget at <a href="https://twitter.com/settings/widgets" target="_blank">https://twitter.com/settings/widgets</a> and copy/paste the id of the widget into this field.', max_length=100, verbose_name='Widget id')),
                ('theme', models.CharField(max_length=5, verbose_name='Theme', choices=[(b'light', 'Light'), (b'dark', 'Dark')])),
                ('width', models.CharField(max_length=4, verbose_name='Width in pixels')),
                ('height', models.CharField(max_length=4, verbose_name='Height in pixels')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
