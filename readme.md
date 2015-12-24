##About


Twitter dropped support for v1.0 of its REST API. Since this was used in DjangoCMS, all of the installations which used this plugin broke.
Hence, this creates a twitter plugin using widgets.


##Installation

- In order to install this plugin, fire up your virtualenv:

	```bash
		pip install cmsplugin-twitter
	```

- And add the this line in INSTALLED_APPS in your base.py
```python
INSTALLED_APPS = (
    'south',
    'project.apps.movies',
    'project.apps.books',
    'project.apps.blog',
    'project.apps.linkedin',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'cms',
    'cms.plugins.text',
    'cms.plugins.picture',
    'cms.plugins.link',
    'cms.plugins.file',
    'cms.plugins.snippet',
    'cms.plugins.googlemap',
    'sekizai',
    'cmsplugin_twitter',
    'menus',
    'mptt',
    'publisher',
    'storages',
    'boto',
    'tinymce',
)
```
considering you have settings.py similar to this:

- After saving them , run migrations:

	```bash
		python manage.py migrate
	```

##How to Use:

- Login to your `twitter` account and go to this url: `https://twitter.com/settings/widgets`

- Create a new widgets and then copy the `twitter handle ` and ` widget_id` from the generated script.

- Enter those two fields in the plugin form and other fields and you are good to go.


##Plugin in Action


This is the plugin working on a Django-CMS site:

![Twitter Plugin](twitter.png)

Enjoy!

