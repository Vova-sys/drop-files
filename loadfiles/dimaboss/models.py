from django.db import models


class Router(models.Model):
    class Meta:
        verbose_name = 'Файлы'
        verbose_name_plural = 'Загрузка файлов'

    specifications = models.FileField(upload_to='router_specifications')
