from django.db import models
from django.urls import reverse_lazy
import random


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент') # blank=True поле не обязательно к заполнению
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации') # auto_now_add=дата не изменяется
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено') # auto_now=дата изменяется при обновлении
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')
    views = models.IntegerField(default=random.randint(2230, 5302))

    def get_absolute_url(self):
    	return reverse_lazy('view_news', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    class Meta:
	    verbose_name = 'Новость'
	    verbose_name_plural = 'Новости'
	    ordering = ['-created_at']


class Category(models.Model):
	title = models.CharField(max_length=50, db_index=True, verbose_name='Название категории')

	def get_absolute_url(self):
		return reverse_lazy('category', kwargs={'category_id': self.pk})

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Категории'
		verbose_name = 'Категория'
		ordering = ['title']
		