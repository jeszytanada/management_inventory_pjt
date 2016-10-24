from django.conf.urls import url
from . import views

app_name = 'products'
urlpatterns = [
    # List /list
    url(r'^list/$', views.ProductListView.as_view(), name='product_list'),
    # Details /27/detail
    url(r'^(?P<pk>[0-9]+)/detail/$', views.ProductDetailView.as_view(), name='product_detail'),
    # /add
    url(r'^add/$', views.ProductCreate.as_view(), name='product_add'),
    # /27/edit
    url(r'^(?P<pk>[0-9]+)/edit/$', views.ProductEdit.as_view(), name='product_edit'),
    # /27/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name='product_delete'),
    # List /search_list
    url(r'^search_list/$', views.ProductSearchListView.as_view(), name='product_search_list'),
]