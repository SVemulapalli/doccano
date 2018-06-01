from django.urls import path

from .views import AnnotationView, AnnotationAPIView, MetaInfoAPI, SearchAPI
from .views import ProjectListView, ProjectDetailView, ProjectAdminView

urlpatterns = [
    path('', ProjectListView.as_view(), name='project-list'),
    path('<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('<int:pk>/admin', ProjectAdminView.as_view()),
    path('<int:project_id>/docs', AnnotationView.as_view()),
    path('<int:project_id>/apis/data', AnnotationAPIView.as_view()),
    path('<int:project_id>/apis/label', MetaInfoAPI.as_view()),
    path('<int:project_id>/apis/search', SearchAPI.as_view()),
]