from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog$', views.post_list, name='post_list'),
   # url(r'^list$', views.list_all, name='list_all'),
]