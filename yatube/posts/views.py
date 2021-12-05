from django.shortcuts import render


def index(request):
    """Обработчик главной страницы"""
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text
    }
    return render(request=request, template_name=template, context=context)


def group_posts(request, slug):
    """Обработчик груп постов"""
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text': text
    }
    return render(request=request, template_name=template, context=context)
