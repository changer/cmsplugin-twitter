from setuptools import setup, find_packages

version = '1.1.0'

setup(
    name='cmsplugin-twitter',
    version=version,
    description='Twitter plugin to work with Django-CMS',
    author='Vinit Kumar',
    author_email='vinit.kumar@changer.nl',
    url='http://github.com/changer/cmsplugin-twitter',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
    ],
)
