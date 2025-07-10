from django.urls import path

from news.views import news_list, news_detail

urlpatterns = [
    path('', news_list, name='home'),
    path('news/<int:pk>/', news_detail, name='detail')
]
