import requests
from django.http import HttpResponse
from django.shortcuts import render

from excepts.utils import menu

# Previous imports and timing middleware should remain unchanged
def stackoverflow(get_response):
    def middleware(request):
        # Этот метод ничего не делает, все, что мы хотим,
        # это обработка исключений
        return get_response(request)

    def process_exception(request, exception):
        url = 'https://api.stackexchange.com/2.2/search'
        params = {
            'site': 'stackoverflow',
            'order': 'desc',
            'sort': 'votes',
            'pagesize': 5,
            'tagged': 'python;django',
            'intitle': str(exception),
        }
        response = requests.get(url, params=params)
        html = []
        for question in response.json()['items']:
            html.append({'link': question['link'], 'title': question['title']})

        return render(request, 'excepts/forErrors.html', {'title': 'Ошибка ' + str(exception), 'exception': str(exception),'menu': menu, 'answers': html})

    middleware.process_exception = process_exception

    return middleware