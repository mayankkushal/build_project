from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.form, name='index'),
	url(r'^login/$', views.ldap_login, name='ldap_login')
]