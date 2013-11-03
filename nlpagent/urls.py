from django.conf.urls import patterns, url
from nlpagent import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^echo/$', views.echo, name='echo'),
)