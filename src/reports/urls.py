from django.urls import path
from .views import (
    create_report_view,
    ReportListView,
    ReportDetailView,
    render_pdf_view,
    UploadTemplateView,
    csv_upload_view
)
from reports_proj.settings import BASE_DIR

app_name = 'reports'

urlpatterns = [
    path('', ReportListView.as_view(), name='main'),
    path('save/', create_report_view, name='create-report'),
    path('upload/', csv_upload_view, name='upload'),
    path('from_file/', UploadTemplateView.as_view(), name='from-file'),
    path('<pk>', ReportDetailView.as_view(), name='detail'),
    path('<pk>/pdf/', render_pdf_view, name='pdf'),
]
