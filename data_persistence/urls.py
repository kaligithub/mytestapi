from django.conf.urls import url
from . import views


urlpatterns = [
    #url(r'^readconfig/$', views.readconfig, name='readconfig'),
    url(r'^keyword_extractor/$', views.keyword_extractor, name='keyword_extractor'),
    url(r'^content_providerjson/$', views.content_providerjson, name='content_providerjson'),
    url(r'^favorite_status/$', views.favorite_status, name='favorite_status'),
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^search/$', views.search, name='search'),
    url(r'^get_allusers/$', views.get_allusers, name='get_allusers'),
    url(r'^get_user_byid/$', views.get_user_byid, name='get_user_byid'),
    
]