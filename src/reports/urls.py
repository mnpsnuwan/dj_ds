from django.urls import path
from .views import (
    create_report_view,
    ReportListView,
    ReportDetailView,
    render_pdf_view
)

app_name = 'reports'

urlpatterns = [
    path('', ReportListView.as_view(), name='main'),
    path('save/', create_report_view, name='create-report'),
    path('pdf/', render_pdf_view, name='pdf'),
    path('<pk>', ReportDetailView.as_view(), name='detail')
]
