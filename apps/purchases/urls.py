from django.conf.urls import url, include
from . import views

app_name = 'purchases'
urlpatterns = [
    # List /list
    url(r'^list', views.PurchaseOrderView.as_view(), name='purchase_order_list'),
    # Details /27/stock_adjustment_detail
     url(r'^(?P<pk>[0-9]+)/detail/$', views.PurchaseOrderDetailView.as_view(), name='purchase_order_detail'),
]