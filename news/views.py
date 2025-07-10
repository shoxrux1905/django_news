from django.shortcuts import render

from news.models import New, Category
from django.shortcuts import get_object_or_404

def news_list(request) :
    news = New.objects.all()
    categories = Category.objects.all()
    context = {
        'datas' : news,
        'categories' : categories
    }
    
    return render(request, 'index.html', context)

def news_detail(request, pk) :
    news = get_object_or_404(New, id=pk)
    context = {
        'news' : news
    }
    
    return render(request, 'detail.html', context)

class Meta :
    ordering = ['-id']