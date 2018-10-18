from django.conf.urls import url
from django.contrib import admin

from .views import (
    PostListAPIview,
    PostDetailAPIview,
    PostUpdateAPIview,
    PostDeleteAPIview,
    PostCreateAPIview,
	)

urlpatterns = [
	url(r'^$', PostListAPIview.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIview.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIview.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/delete/$', PostDeleteAPIview.as_view(), name='delete'),
    url(r'^create/$',PostCreateAPIview.as_view(), name='create'),
]
