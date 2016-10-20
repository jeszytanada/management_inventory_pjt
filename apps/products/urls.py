from django.conf.urls import url
from . import views

app_name = 'products'
urlpatterns = [
    # List pjt_inventory/product_list
    url(r'^list', views.ProductListView.as_view(), name='product_list'),
    # Details pjt_inventory/27/product_detail
    url(r'^(?P<pk>[0-9]+)/detail/$', views.ProductDetailView.as_view(), name='product_detail'),
    # /pjt_inventory/product_add
    url(r'^add/$', views.ProductCreate.as_view(), name='product_add'),
    # /pjt_inventory/27/product_edit
    url(r'^(?P<pk>[0-9]+)/edit/$', views.ProductEdit.as_view(), name='product_edit'),
    # /pjt_inventory/27/product_delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ProductDelete.as_view(), name='product_delete'),
]