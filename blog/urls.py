from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$', 'index', name='index'),
)

