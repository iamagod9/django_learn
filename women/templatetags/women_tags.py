from django import template
from women.models import *

register = template.Library()

@register.inclusion_tag('women/nav_menu.html')
def show_nav_menu():
    menu = [
        {'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
    ]

    posts = Women.objects.all()
    return {'posts': posts,
            'menu': menu,
            'title': 'Main page',
            'cat_selected': 0,}

@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {'cats': cats, 'cat_selected': cat_selected}