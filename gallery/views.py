from django.views.generic import ListView, DetailView, TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect


from .models import Work, Category, Service


class HomeView(ListView):
    model = Work
    template_name = 'gallery/home.html'
    context_object_name = 'works'

    def get_queryset(self):
        return (
            Work.objects
            .filter(is_published=True)
            .select_related('category')
            .order_by('category__order', '-created_at')
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('order', 'name')
        return context


class WorkDetailView(DetailView):
    model = Work
    template_name = 'gallery/work_detail.html'
    context_object_name = 'work'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'


class ServicesView(ListView):
    model = Service
    template_name = 'gallery/services.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.filter(is_active=True).order_by('order')


# --- Статические страницы ---

class AboutView(TemplateView):
    template_name = 'gallery/about.html'


class HelpView(TemplateView):
    template_name = 'gallery/help.html'


# --- Авторизация / регистрация ---

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'gallery/register.html'
    success_url = reverse_lazy('home')


# --- Миксин для форм добавления контента ---

class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff


# --- Формы добавления категорий и работ ---

class CategoryCreateView(StaffRequiredMixin, CreateView):
    model = Category
    fields = ['name', 'slug', 'description', 'order']
    template_name = 'gallery/category_form.html'
    success_url = reverse_lazy('home')


class WorkCreateView(StaffRequiredMixin, CreateView):
    model = Work
    fields = [
        'title',
        'slug',
        'category',
        'preview_image',
        'description',
        'created_at',
        'is_published',
    ]
    template_name = 'gallery/work_form.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')

class ServiceCreateView(StaffRequiredMixin, CreateView):
    model = Service
    fields = ['title', 'description', 'price_from', 'is_active', 'order']
    template_name = 'gallery/service_form.html'
    success_url = reverse_lazy('services')

class ContentDashboardView(StaffRequiredMixin, TemplateView):
    template_name = 'gallery/content_dashboard.html'
