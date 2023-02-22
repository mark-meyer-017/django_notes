from django.contrib import admin
from .models import *


# класс, в котором можно указать что будет отображаться из данного приложения
class NoteModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'note_title',
        'created_at',
        'updated_at',
        'is_published',
        'category',
    )

    # список полей которые станут ссылками на запись
    list_display_links = (
        'id',
        'note_title',
    )

    # список полей, по которым можно производить поиск в админке
    search_fields = (
        'note_title',
        'note_content',
    )


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
    )

    list_display_links = (
        'id',
        'title',
    )

    search_fields = ('title',)


# Регистрация моделей для отображения в админке, NotemodelAdmin так же нужно
# регистрировать, но указывать после приложения noteModel
admin.site.register(NoteModel, NoteModelAdmin)
admin.site.register(CategoryModel, CategoryModelAdmin)
