from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView  # импортируем необходимые дженерики
    # импортируем класс, который говорит нам о том, что в этом представлении мы будем выводить список объектов из БД
     # импортируем класс получения деталей объекта
from .models import Author, Category, Post, PostCategory, Comment
from datetime import datetime
# D5
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from .filters import PostFilter
from django.shortcuts import render
from django.views import View  # импортируем простую вьюшку
from django.core.paginator import Paginator  # импортируем класс, позволяющий удобно осуществлять постраничный вывод
from .forms import PostForm  # импортируем нашу форму

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
    paginate_by = 1
    form_class = PostForm  # добавляем форм класс, чтобы получать доступ к форме через метод POST

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()  # добавим переменную текущей даты time_now , но значение текущего локального времени, а не utf
        context['filter'] = PostFilter(self.request.GET,
                                          queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        # context['categoryType'] = get_categoryType_display()

        context['postCategories'] = Category.objects.all()

        context['form'] = PostForm()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)


# создаём представление, в котором будут детали конкретного отдельного товара
class PostDetail(DetailView):
    model = Post  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
    template_name = 'post.html'  # название шаблона будет product.html
    context_object_name = 'post'  # название объекта. в нём будет
    # commetsset = Comment.objects.filter(commentPost= 'Post.id').order_by('dateCreation').values('dateCreation', 'commentUser','rating', 'text')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.now()  # добавим переменную текущей даты time_now
        context['comment_list'] = Comment.objects.filter(commentPost=self.kwargs['pk'])

        return context


class PostSearch(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'search.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    context_object_name = 'news'
    #context_object_name = 'search'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.all()  # Н

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context[
            'time_now'] = datetime.now()  # добавим переменную текущей даты time_now , но значение текущего локального времени, а не utf
        context['filter'] = PostFilter(self.request.GET,
                                       queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context




# дженерик для создания объекта. Надо указать только имя шаблона и класс формы, который мы написали в прошлом юните. Остальное он сделает за вас
class PostCreateView(CreateView):
    template_name = 'post_create.html'
    form_class = PostForm


# дженерик для редактирования объекта
class PostUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'post_create.html'
    form_class = PostForm

    # метод get_object мы используем вместо queryset, чтобы получить информацию об объекте, который мы собираемся редактировать
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# дженерик для удаления товара
class PostDeleteView(DeleteView):
    template_name = 'post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'









class PostSearch1(ListView):
    model = Post  # указываем модель, объекты которой мы будем выводить
    template_name = 'search.html'  # указываем имя шаблона, в котором будет лежать HTML, в котором будут все инструкции о том, как именно пользователю должны вывестись наши объекты
    #context_object_name = 'search'  # это имя списка, в котором будут лежать все объекты, его надо указать, чтобы обратиться к самому списку объектов через HTML-шаблон
    queryset = Post.objects.all()  # Н
    #form_class = PostForm


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

