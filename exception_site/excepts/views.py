from django.http import HttpResponseNotFound
from django.shortcuts import render
from .utils import menu, list_exceptions


# Create your views here.

def home(request):
    return render(request, 'excepts/mainpage.html', {'title': 'Главная страница', 'menu': menu, 'list_of_exceptions': list_exceptions})

def pageNotFound(request, exception):
    context = {
        'title': 'Страница не найдена',
        'menu': menu,
    }
    return HttpResponseNotFound(render(request, 'excepts/404.html', context=context))

def IndexErr(request):
    raise IndexError('Index error')

def AtttributeError(request):
    raise AttributeError('Attribute error')

def ImportErr(request):
    raise ImportError('Import error')

def ZeroDivErr(request):
    raise ZeroDivisionError('ZeroDivision Error')

def EOFErr(request):
    raise EOFError('EOF Error')