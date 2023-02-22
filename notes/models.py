from django.db import models
from django.urls import reverse


# создает модель, которая формирует таблицу в базе данных
class NoteModel(models.Model):
    note_title = models.CharField(max_length=150,
                                  db_index=True,
                                  verbose_name='Заголовок')
    note_content = models.TextField(blank=True,
                                    verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name="Обновлено")
    note_photo = models.ImageField(upload_to='note_photos/%Y/%m/%d/',
                                   verbose_name="Фото_заметки",
                                   blank=True)
    is_published = models.BooleanField(default=True,
                                       verbose_name="Опубликовано")
    category = models.ForeignKey("CategoryModel",
                                 on_delete=models.PROTECT,
                                 verbose_name='Категория')

    # выстраивает ссылку на обьект
    def get_absolute_url(self):
        return reverse('view_note', kwargs={'note_id': self.pk})

    # формирует строковое представление при запросе информации об обьекте
    def __str__(self):
        return self.note_title

    # класс который корректирует имя модели в единственном и множественном
    # числе
    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'
        # сортировка списка по указанным полям (слева имеет больший приоритет)
        ordering = ['-created_at', 'note_title']


class CategoryModel(models.Model):
    title = models.CharField(max_length=150,
                             verbose_name='Категория',
                             db_index=True)
    photo = models.ImageField(upload_to='category_photos/%Y/%m/%d/',
                              verbose_name='Фото_категории',
                              blank=True)

    def get_absolute_url(self):
        return reverse('view_category', kwargs={'category_id': self.pk})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
