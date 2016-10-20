from django.conf.urls import url
from . import views

app_name = 'category'
urlpatterns = [
    # List pjt_inventory/category_list
    url(r'^list/$', views.CategoryListView.as_view(), name='category_list'),
    # List pjt_inventory/27/category_sub_list
    url(r'^(?P<pk>[0-9]+)/sub_list/$', views.CategorySubListView.as_view(), name='category_sub_list'),
    # /pjt_inventory/category_add
    url(r'^add/$', views.CategoryCreate.as_view(), name='category_add'),
    # List pjt_inventory/27/category_product
    url(r'^(?P<pk>[0-9]+)/product/$', views.CategoryProductListView.as_view(), name='category_product'),
    # /pjt_inventory/27/category_edit
    url(r'^(?P<pk>[0-9]+)/edit/$', views.CategoryEdit.as_view(), name='category_edit'),
]