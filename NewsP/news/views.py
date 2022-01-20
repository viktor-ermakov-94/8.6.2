from django.views.generic import ListView, DetailView
    # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
     # импортируем класс получения деталей объекта
from .models import Author, Category, Post, PostCategory, Comment
from datetime import datetime

class PostList(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'allposts.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'posts'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-id')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now
        #context['value1'] = None   добавим ещё одну пустую переменную, чтобы на её примере посмотреть работу другого фильтра
        #context['countposts'] = 'posts|length'
        return context


class PostList1(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'news.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.order_by('-dateCreation') #Новости должны выводиться в порядке от более свежей до самой старой

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()  # добавим переменную текущей даты time_now , но значение текущего локального времени, а не utf

        return context


# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post.html'  # название шаблона будет product.html
    context_object_name = 'post'  # название объекта. в нём будет
    #commetsset = Comment.objects.filter(commentPost= 'Post.id').order_by('dateCreation').values('dateCreation', 'commentUser','rating', 'text')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()  # добавим переменную текущей даты time_now

        return context

#class CommentList1(ListView):
#    model = Comment  # указываем модель, объекты которой мы будем выводить
#    template_name = 'post.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
#    context_object_name = 'comments'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    #queryset = Comment.objects.order_by('-dateCreation') #Новости должны выводиться в порядке от более свежей до самой старой
 #   queryset = Comment.objects.filter(commentPost='post').order_by('dateCreation').values('dateCreation', 'commentUser', 'rating', 'text')


 #   def get_context_data(self, **kwargs):
 #       context = super().get_context_data(**kwargs)
#
 #       return context

