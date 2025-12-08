from django.contrib import admin
from .models import Category, Work, WorkImage, Service


class WorkImageInline(admin.TabularInline):
    model = WorkImage
    extra = 1


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_published')
    list_filter = ('category', 'is_published')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [WorkImageInline]


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'price_from', 'is_active', 'order')
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('title',)}
