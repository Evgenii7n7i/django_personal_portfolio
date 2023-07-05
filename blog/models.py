from django.db import models


class Blog(models.Model):
    title_blog = models.CharField(max_length=100, verbose_name='Заголовок блога')
    description_blog = models.TextField(verbose_name='Описание')
    date = models.DateTimeField(auto_now = False, verbose_name='Дата')
    
    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'

    def __str__(self):
        return self.title_blog 