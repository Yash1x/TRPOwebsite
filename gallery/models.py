from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField("Название", max_length=100)
    slug = models.SlugField("Слаг", unique=True)
    description = models.TextField("Описание", blank=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Work(models.Model):
    title = models.CharField("Название работы", max_length=200)
    slug = models.SlugField("Слаг", unique=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name='works',
        verbose_name="Категория"
    )
    preview_image = models.ImageField(
        "Превью",
        upload_to='works/previews/'
    )
    description = models.TextField("Описание")
    created_at = models.DateField("Дата создания", null=True, blank=True)
    is_published = models.BooleanField("Опубликовано", default=True)

    class Meta:
        ordering = ['-created_at', 'title']
        verbose_name = "Работа"
        verbose_name_plural = "Работы"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('work_detail', kwargs={'slug': self.slug})


class WorkImage(models.Model):
    work = models.ForeignKey(
        Work,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="Работа"
    )
    image = models.ImageField(
        "Изображение",
        upload_to='works/gallery/'
    )
    caption = models.CharField("Подпись", max_length=200, blank=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ['order']
        verbose_name = "Изображение работы"
        verbose_name_plural = "Изображения работы"

    def __str__(self):
        return f"{self.work.title} #{self.order}"


class Service(models.Model):
    title = models.CharField("Название услуги", max_length=200)
    slug = models.SlugField("Слаг", unique=True)
    short_description = models.CharField("Краткое описание", max_length=255)
    description = models.TextField("Подробное описание", blank=True)
    price_from = models.DecimalField(
        "Цена от",
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )
    is_active = models.BooleanField("Активна", default=True)
    order = models.PositiveIntegerField("Порядок", default=0)

    class Meta:
        ordering = ['order', 'title']
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"

    def __str__(self):
        return self.title

