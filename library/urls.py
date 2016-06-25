from django.conf.urls import url

from . import views

app_name = 'library'
urlpatterns = [
    url(r'^$', views.IndexView, name='publisher'),
    url(r'^publishers/$', views.PublisherView, name='publisher'),
    url(r'^publishers/create/$', views.add_publisher, name='addpublisher'),
    url(r'^publishers/(?P<id>[0-9]+)/delete/$', views.del_publisher, name='delpublisher'),
    url(r'^publishers/(?P<id>[0-9]+)/edit/$', views.edit_publisher, name='editpublisher'),
    url(r'^authors/$', views.AuthorView, name='author'),
    url(r'^books/$', views.BookView, name='book'),
    url(r'^userprofiles/$', views.UserProfileView, name='userprofile'),
    url(r'^issues/$', views.IssueView, name='issue'),

]
