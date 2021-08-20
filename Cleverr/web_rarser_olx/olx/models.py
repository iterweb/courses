from django.db import models


class OlxAdvert(models.Model):
    title = models.CharField(max_length=250, unique=True, verbose_name='Заголовок')
    price = models.CharField(max_length=250, verbose_name='Цена')
    published = models.CharField(max_length=250, verbose_name='Дата публикации')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['-time_create']
