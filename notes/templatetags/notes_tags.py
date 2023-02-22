from django import template

from notes.models import CategoryModel

# регистрация тэгов
register = template.Library()


# # simple tag передает данные
# @register.simple_tag(name='get_list_categories')
# def get_categories():
#     return CategoryModel.objects.all()

# inclusion tag не только передает данные, но и рендерит их в шаблон
@register.inclusion_tag('notes/list_categories.html')
def show_categories():
    categories = CategoryModel.objects.all()
    return {'categories': categories}