# Generated by Django 5.0 on 2023-12-12 12:36

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Identificador')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado às')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado às')),
                ('title', models.CharField(max_length=150, verbose_name='Título')),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d', verbose_name='Foto')),
                ('description', models.TextField(max_length=500, verbose_name='Descrição')),
                ('visible', models.BooleanField(default=True, verbose_name='Visivel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Proprietário')),
            ],
            options={
                'ordering': ['-created_at'],
                'abstract': False,
            },
        ),
    ]
