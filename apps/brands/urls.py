from django.conf.urls import url
from . import views

app_name = 'brands'
urlpatterns = [
    #url(r'^index/$', views.IndexView.as_view(), name='index'),
    # List /list
    url(r'^list/$', views.BrandListView.as_view(), name='brand_list'),
    # Details 27/detail
    url(r'^(?P<pk>[0-9]+)/detail/$', views.BrandDetailView.as_view(), name='brand_detail'),
    # /brand_add
    url(r'^add/$', views.BrandCreate.as_view(), name='brand_add'),
    # /27/edit
    url(r'^(?P<pk>[0-9]+)/edit/$', views.BrandEdit.as_view(), name='brand_edit'),
    # /27/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.BrandDelete.as_view(), name='brand_delete'),
]