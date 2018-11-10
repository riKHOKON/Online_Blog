from django.conf.urls import url

from .views import (
    PostListView,
    PostDetailSlugView,
    )

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailSlugView.as_view(), name='detail'), 
]
