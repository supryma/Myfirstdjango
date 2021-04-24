from django.shortcuts import render


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'bmw',
            'age': '2k',
            'hobby': 'eat shit'
        }
    }
    return render(request, 'zeroapp/index.html', data)


def about(request):
    return render(request, 'zeroapp/about.html')