from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import NoteForm, CategoryForm


# Передает данные модели NoteModel в шаблон index.html
def index(request):
    notes = NoteModel.objects.all()
    context = {'notes': notes,
               'title': 'Конспект',
               }
    return render(request, "notes/index.html", context)


# передает данные в шаблон category.html и получает  primary key в виде
#  category_id
def get_category(request, category_id):
    notes = NoteModel.objects.filter(category_id=category_id)
    category = CategoryModel.objects.get(pk=category_id)
    context = {
        'notes': notes,
        'title': 'Конспект',
        'category': category,
    }
    return render(request,
                  template_name='notes/category.html',
                  context=context)


def view_note(request, note_id):
    # one_note = NoteModel.objects.get(pk=note_id)
    one_note = get_object_or_404(NoteModel, pk=note_id)
    context = {
        'one_note': one_note
    }
    return render(request,
                  template_name='notes/note.html',
                  context=context)


def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST,request.FILES)
        if form.is_valid():
            note = form.save()
            return redirect(note)
    else:
        form = NoteForm
    return render(request, 'notes/add_note.html', {'form': form})


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CategoryForm
    return render(request, 'notes/add_category.html', {'form': form})
