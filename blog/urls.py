from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    re_path(r'^singl_post/(?P<post_id>[0-9]+)$', singl_post)
]
