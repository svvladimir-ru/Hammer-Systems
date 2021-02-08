from django.shortcuts import render


def index(request):
    """Вывод главной страницы"""
    return render(request, 'index.html')
