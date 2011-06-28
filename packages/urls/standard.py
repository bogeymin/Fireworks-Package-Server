"""
Module URL configuration for packages.
"""
from django.conf.urls.defaults import patterns

urlpatterns = patterns('application.packages.views',
    (r'^$','index'),
    (r'^testing/$','testing'),
    (r'^(?P<package_name>[-\w]+)/$','package'),
    (r'^(?P<package_name>[-\w]+)/(?P<version_number>[-\w\d\.]+)/$','package'),
)
