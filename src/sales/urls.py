from django.urls import path
from .views import (
    home_view,
    SaleListView,
    SaleDetailView,
    # sale_list_view,
    # sale_detail_view,
)

app_name = 'sales'

urlpatterns = [
    path('', home_view, name='home'),
    path('sales/', SaleListView.as_view(), name='sales'),
    path('sales/<pk>/', SaleDetailView.as_view(), name='detail'),

    # For function methods
    # path('sales/', sale_list_view, name='list'),
    # path('sales/<pk>/', sale_detail_view, name='detail')
]