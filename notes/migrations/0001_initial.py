# Generated by Django 3.1.5 on 2021-01-31 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Категория')),
                ('photo', models.ImageField(blank=True, upload_to='category_photos/%Y/%m/%d/', verbose_name='Фото_категории')),
            ],
        ),
        migrations.CreateModel(
            name='Note_model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note_title', models.CharField(db_index=True, max_length=150, verbose_name='Заголовок')),
                ('note_content', models.TextField(blank=True, verbose_name='Контент')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('note_photo', models.ImageField(blank=True, upload_to='note_photos/%Y/%m/%d/', verbose_name='Фото_заметки')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='notes.category_model', verbose_name='Категория')),
            ],
        ),
    ]
