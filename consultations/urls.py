from django.urls import path
from .views import ConsultationListCreateView

urlpatterns = [
    path('consultations/', ConsultationListCreateView.as_view(), name='consultation-list-create'),
]
