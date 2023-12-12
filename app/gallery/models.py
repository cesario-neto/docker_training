from django.db import models
from core.models import BaseModel
from django.conf import settings


class Photo(BaseModel):
    title = models.CharField(verbose_name='Título', max_length=150)
    photo = models.ImageField(
        verbose_name='Foto',
        upload_to='photo/%Y/%m/%d',
        blank=False,
        null=False
    )
    description = models.TextField(verbose_name='Descrição', max_length=500)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name='Proprietário',
    )
    visible = models.BooleanField(verbose_name='Visivel', default=True)
