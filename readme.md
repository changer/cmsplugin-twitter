##About

[![Build Status](https://travis-ci.org/vinitcool76/cmsplugin-twitter.png?branch=master)](https://travis-ci.org/vinitcool76/cmsplugin-twitter)

Twitter recently dropped support for v1.0 of its REST API. Since this was used in DjangoCMS, all of the installations which used this plugin broke.
Hence, this is an attempt to create a similar plugin using widgets.


##Installation

- In order to install this plugin, fire up your virtualenv:

	```bash
		pip install cmsplugin-twitter
	```

- And add the this line in installed apps in your base.py

	```python
		'cmsplugin_twitter',
	```

- After saving them , run:

	```bash
		python manage.py syncdb
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



