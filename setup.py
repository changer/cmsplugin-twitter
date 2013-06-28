from setuptools import setup, find_packages

version = '1.0.4'

setup(
    name='cmsplugin-twitter',
    version=version,
    description='Twitter plugin to work with Django-CMS',
    author='Vinit Kumar',
    author_email='vinit.kumar@changer.nl',
    url='http://github.com:vinitcool76/cmsplugin-twitter.git',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
    ],
)
