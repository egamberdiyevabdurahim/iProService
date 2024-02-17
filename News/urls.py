from django.urls import path

from .views import Haqida, CreateNews, OpenNews, EditNews, DeleteNews


urlpatterns = [
    path('posts/<slug:slug>/', OpenNews.as_view(), name='opennews'),
    path('create/', CreateNews.as_view(), name='create'),
    path('haqida/', Haqida.as_view(), name='haqida'),
    path('edit/<int:id>/', EditNews.as_view(), name='edit'),
    path('delete/<int:id>/', DeleteNews.as_view(), name='delete'),
]