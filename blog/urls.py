from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$', 'index', name='index'),
    url(r'^(?P<post_id>\d+)$', 'show', name='show'),
)

