from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^', views.BasicView.as_view(), name='index')
]