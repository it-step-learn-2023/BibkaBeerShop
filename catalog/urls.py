from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('beer', beer),
    path('wine', wine),
    path('sidr', sidr),
    path('zakys', zakys),
    path('add_product', add_product),
    re_path(r'^edit_product/(?P<product_id>[0-9]+)$', edit_product),
    path('ajax_del_product', ajax_del_product),
    re_path(r'^singl_product/(?P<product_id>[0-9]+)$', singl_product),
]
