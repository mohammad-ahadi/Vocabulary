from django.shortcuts import render

from .models import Word
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    context = {}
    words_list = Word.objects.all()
    paginator = Paginator(words_list, 10)
    page = request.GET.get('page')
    try:
        words = paginator.page(page)
    except PageNotAnInteger:
        words = paginator.page(1)
    except EmptyPage:
        words = paginator.page(paginator.num_pages)
    context['words'] = words
    return render(request, 'app/index.html', context)
