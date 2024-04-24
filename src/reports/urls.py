from django.urls import path
from .views import (
    create_report_view,
    ReportListView,
    ReportDetailView
)

app_name = 'reports'

urlpatterns = [
    path('', ReportListView.as_view(), name='main'),
    path('save/', create_report_view, name='create-report'),
    path('<pk>', ReportDetailView.as_view(), name='detail')
]
