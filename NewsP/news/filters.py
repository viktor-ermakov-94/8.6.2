from django_filters import FilterSet  # импортируем filterset, чем-то напоминающий знакомые дженерики
from .models import Post

# 	позже какой-либо даты;
# 	по названию;
# 	по имени пользователя автора;
# 	всё вместе

class PostFilter(FilterSet):
    class Meta:
        model = Post
        fields = {

            'dateCreation': ['gt'],  # позже какой-либо даты, что указал пользователь
            'title': ['icontains'],  # мы хотим чтобы нам выводило имя хотя бы отдалённо похожее на то что запросил пользователь
            'author': ['exact'],
            'categoryType': ['exact'],
            'postCategory': ['exact'],
         #   'author.authorUser.username': ['icontains'],  # по имени пользователя автора - по фрагменту
          #  'category':[]
        }