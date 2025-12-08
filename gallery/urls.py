from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('work/<slug:slug>/', views.WorkDetailView.as_view(), name='work_detail'),
    path('services/', views.ServicesView.as_view(), name='services'),
]
