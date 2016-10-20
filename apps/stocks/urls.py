from django.conf.urls import url, include
from . import views

app_name = 'stocks'
urlpatterns = [
    # List /list
    url(r'^list', views.StockAdjustmentView.as_view(), name='stock_adjustment_list'),
    # Details /27/stock_adjustment_detail
     url(r'^(?P<pk>[0-9]+)/detail/$', views.StockAdjustmentDetailView.as_view(), name='stock_adjustment_detail'),
    # # /pjt_inventory/supplier_add
    # url(r'^add/$', views.SupplierCreate.as_view(), name='supplier_add'),
    # # /pjt_inventory/27/supplier_edit
    # url(r'^(?P<pk>[0-9]+)/edit/$', views.SupplierEdit.as_view(), name='supplier_edit'),
    # # /pjt_inventory/27/supplier_delete
    # url(r'^(?P<pk>[0-9]+)/delete/$', views.SupplierDelete.as_view(), name='supplier_delete'),
    # # List pjt_inventory/supplier_contact_list
    # url(r'^(?P<pk>[0-9]+)/contact_list', views.SupplierContactListView.as_view(), name='supplier_contact_list'),
    # # /pjt_inventory/supplier_contact_add
    # url(r'^supplier_contact_add/$', views.SupplierContactCreate.as_view(), name='supplier_contact_add'),
    # # /pjt_inventory/27/supplier_contact_edit
    # url(r'^(?P<pk>[0-9]+)/contact_edit/$', views.SupplierContactEdit.as_view(), name='supplier_contact_edit'),
]