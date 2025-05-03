from django.contrib import admin

from .models import Group, Post


class BaseAdmin(admin.ModelAdmin):
    """Базовый класс админ-панели с общими настройками."""

    empty_value_display = ' '


@admin.register(Post)
class PostAdmin(BaseAdmin):
    list_display = (
        'pk',
        'pub_date',
        'author',
        'group',
        'image',
    )
    search_fields = ('text',)
    list_filter = ('pub_date',)


@admin.register(Group)
class GroupAdmin(BaseAdmin):
    list_display = (
        'title',
        'slug',
        'description',
    )
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ('slug',)
    list_filter = ('title',)
