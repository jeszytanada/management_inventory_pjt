from django.conf.urls import url
from . import views

app_name = 'brands'
urlpatterns = [
    #url(r'^index/$', views.IndexView.as_view(), name='index'),
    # List pjt_inventory/brand_list
    url(r'^list/$', views.BrandListView.as_view(), name='brand_list'),
    # Details pjt_inventory/27/brand_detail
    url(r'^(?P<pk>[0-9]+)/detail/$', views.BrandDetailView.as_view(), name='brand_detail'),
    # /pjt_inventory/brand_add
    url(r'^add/$', views.BrandCreate.as_view(), name='brand_add'),
    # /pjt_inventory/27/brand_edit
    url(r'^(?P<pk>[0-9]+)/edit/$', views.BrandEdit.as_view(), name='brand_edit'),
    # /pjt_inventory/27/brand_delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.BrandDelete.as_view(), name='brand_delete'),
]