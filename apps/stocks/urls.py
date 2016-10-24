from django.conf.urls import url, include
from . import views

app_name = 'stocks'
urlpatterns = [
    # List /list
    url(r'^list', views.StockAdjustmentView.as_view(), name='stock_adjustment_list'),
    # Details /27/stock_adjustment_detail
     url(r'^(?P<pk>[0-9]+)/detail/$', views.StockAdjustmentDetailView.as_view(), name='stock_adjustment_detail'),
]