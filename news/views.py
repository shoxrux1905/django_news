
from django.shortcuts import redirect, render
from django.urls import reverse

from news.forms import AddNewsForm
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
    categories = Category.objects.all()
    context = {
        'news' : news,
        'categories': categories,
    }
    
    return render(request, 'detail.html', context)

def add_news(request) :
    news_form = AddNewsForm()
    categories = Category.objects.all()
    data = {
        'categories': categories,
        'news_form': news_form,
    }
    if request.method == 'GET':
        return render(request, 'add_news.html', data)
    elif request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else: 
            print(form.errors)
        return redirect(reverse('home'))


def edit_news(request, pk):
    news = get_object_or_404(New, pk=pk)
    categories = Category.objects.all()

    if request.method == 'POST':
        news.title = request.POST['title']
        news.content = request.POST['content']
        news.category_id = request.POST['category']

        if 'image' in request.FILES:
            news.image = request.FILES['image']

        news.save()
        return redirect('detail', news.id)

    return render(request, 'edit_news.html', {
        'news': news,
        'categories': categories
    })

def delete_news(request, pk):
    news = get_object_or_404(New, pk=pk)

    if request.method == 'POST':
        news.delete()
        return redirect('home')

    return render(request, 'delete_news.html', {'news': news})
