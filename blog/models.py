from django.db import models

# Create your models here.
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Наименование')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_up = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='Изображение', blank=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Наименование категории')
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_post', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'category_id': self.pk})

    class Meta:
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']
