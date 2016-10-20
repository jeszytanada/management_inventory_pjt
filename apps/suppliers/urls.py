from django.conf.urls import url, include
from . import views

app_name = 'suppliers'
urlpatterns = [
    # List /list
    url(r'^list', views.SupplierListView.as_view(), name='supplier_list'),
    # Details /27/detail
    url(r'^(?P<pk>[0-9]+)/detail/$', views.SupplierDetailView.as_view(), name='supplier_detail'),
    # /add
    url(r'^add/$', views.SupplierCreate.as_view(), name='supplier_add'),
    # /27/edit
    url(r'^(?P<pk>[0-9]+)/edit/$', views.SupplierEdit.as_view(), name='supplier_edit'),
    # /27/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.SupplierDelete.as_view(), name='supplier_delete'),
    # List /contact_list
    url(r'^(?P<pk>[0-9]+)/contact_list', views.SupplierContactListView.as_view(), name='supplier_contact_list'),
    # /contact_add
    url(r'^supplier_contact_add/$', views.SupplierContactCreate.as_view(), name='supplier_contact_add'),
    # /27/contact_edit
    url(r'^(?P<pk>[0-9]+)/contact_edit/$', views.SupplierContactEdit.as_view(), name='supplier_contact_edit'),
]