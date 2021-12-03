from django.shortcuts import HttpResponse


def index(request):
    """Обработчик главной страницы"""
    if request.method == 'GET':
        return HttpResponse('Hello World')


def group_posts(request, slug):
    """Оюработчик груп постов"""
    if request.method == 'GET':
        return HttpResponse(f'THIS GROUPS PAGE - {slug}')
