from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),

    path('work/<slug:slug>/', views.WorkDetailView.as_view(), name='work_detail'),
    path('services/', views.ServicesView.as_view(), name='services'),

    # Статические страницы
    path('about/', views.AboutView.as_view(), name='about'),
    path('help/', views.HelpView.as_view(), name='help'),

    # Авторизация
    path('login/', auth_views.LoginView.as_view(
        template_name='gallery/login.html'
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
    ), name='logout'),
    path('register/', views.RegisterView.as_view(), name='register'),

    # Добавление контента
    path('category/add/', views.CategoryCreateView.as_view(), name='category_add'),
    path('work/add/', views.WorkCreateView.as_view(), name='work_add'),
]
