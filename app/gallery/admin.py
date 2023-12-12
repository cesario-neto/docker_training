from django.contrib import admin
from .models import Photo
from django.utils.html import format_html
from utils.images import get_new_width_and_height


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = 'title', 'owner', 'photo', 'visible',
    search_fields = 'title',
    list_filter = 'created_at', 'updated_at', 'visible',

    def display_photo(self, obj):
        width, height = get_new_width_and_height(obj.photo.path)
        return format_html(f'<img src="{obj.photo.url}" alt="" width="{width}" height="{height}">')

    readonly_fields = ['display_photo']
