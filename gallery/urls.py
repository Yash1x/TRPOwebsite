from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # Главная
    path('', views.HomeView.as_view(), name='home'),

    # Публичные страницы
    path('services/', views.ServicesView.as_view(), name='services'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('help/', views.HelpView.as_view(), name='help'),

    # Авторизация
    path('login/', auth_views.LoginView.as_view(
        template_name='gallery/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    path('add/', views.ContentDashboardView.as_view(), name='content_dashboard'),


    # Добавление данных
    path('category/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('work/add/', views.WorkCreateView.as_view(), name='work_add'),
    path('service/add/', views.ServiceCreateView.as_view(), name='service_add'),

    # Детальная страница работы *
    path('work/<slug:slug>/', views.WorkDetailView.as_view(), name='work_detail'),
]
