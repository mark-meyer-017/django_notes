from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='view_category'),
    path('note/<int:note_id>', view_note, name='view_note'),
    path('note/add_note', add_note, name='add_note'),
    path('note/add_category', add_category, name='add_category'),
]
