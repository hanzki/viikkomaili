from django.conf.urls import patterns, url

from weeklyMail import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^(?P<item_id>\d+)$', views.editItem, name='edit'),

)