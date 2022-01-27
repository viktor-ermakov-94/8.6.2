from django.urls import path
from .views import PostList, PostDetail, PostList1, PostSearch, PostCreateView, PostUpdateView, PostDeleteView
    # CommentList1  # импортируем наше представление
urlpatterns = [
    # path — означает путь. В данном случае путь ко всем товарам у нас останется пустым, позже станет ясно, почему
    path('', PostList1.as_view()),
    # path('', PostList.as_view()),
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view. Для этого вызываем метод as_view
    path('<int:pk>', PostDetail.as_view(), name='post'),  # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
    path('search/', PostSearch.as_view(), name = 'search' ), # 1.	Добавьте страничку /news/search. на ней должна быть реализована возможность пользователя искать новости по определённым критериям.

    path('add/', PostCreateView.as_view(), name='post_create'),  # Ссылка на создание товара
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
]