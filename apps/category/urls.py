from django.conf.urls import url
from . import views

app_name = 'category'
urlpatterns = [
    # List /list
    url(r'^list/$', views.CategoryListView.as_view(), name='category_list'),
    # List /27/sub_list
    url(r'^(?P<pk>[0-9]+)/sub_list/$', views.CategorySubListView.as_view(), name='category_sub_list'),
    # /add
    url(r'^add/$', views.CategoryCreate.as_view(), name='category_add'),
    # List /27/product
    url(r'^(?P<pk>[0-9]+)/product/$', views.CategoryProductListView.as_view(), name='category_product'),
    # /27/edit
    url(r'^(?P<pk>[0-9]+)/edit/$', views.CategoryEdit.as_view(), name='category_edit'),
]