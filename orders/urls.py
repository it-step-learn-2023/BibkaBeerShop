from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', index),
    path('ajax_cart', ajax_cart),
    path('ajax_cart_count', ajax_cart_count),
    path('ajax_cart_display', ajax_cart_display),
    path('ajax_del_order', ajax_del_order),
    re_path(r'^bill/(?P<sel_list>[0-9\,]{3,})$', bill),

]
