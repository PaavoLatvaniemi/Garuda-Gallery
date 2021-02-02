from django.urls import path, include
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.photo_list.as_view()),
    url(r'^(?P<photo_id>[0-9]+)$', views.detail, name='detail'),
    url(r'^(?P<photo_id>[0-9]+)/delete$', views.delete, name='delete')
]
