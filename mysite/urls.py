from django.conf.urls import url
from . import views
from django.views.static import serve

app_name = 'mysite'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^upload/$', views.upload_file, name='upload_file'),
    url(r'^view/$', views.user_view, name='user_view'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^register/$', views.register, name='register'),
    url(r'^images/(?P<path>.*)$', serve, {'document_root': 'images'}),
]