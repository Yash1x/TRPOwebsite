from django.views.generic import ListView, DetailView
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
    slug_field = 'slug'          # по какому полю искать
    slug_url_kwarg = 'slug'      # как параметр называется в url-паттерне
class ServicesView(ListView):
    model = Service
    template_name = 'gallery/services.html'
    context_object_name = 'services'

    def get_queryset(self):
        return Service.objects.filter(is_active=True).order_by('order')

