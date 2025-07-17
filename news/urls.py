from django.urls import path

from news import views
from news.views import add_news, news_list, news_detail

urlpatterns = [
    path('', news_list, name='home'),
    path('news/<int:pk>/', news_detail, name='detail'),
    path('add/', add_news, name='add_news'),
    path('edit/<int:pk>/', views.edit_news, name='edit_news'),
    path('delete/<int:pk>/', views.delete_news, name='delete_news'),

]
