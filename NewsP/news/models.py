from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.db.models import Sum

# Create your models here.
# 1.	Модель Author
# Модель, содержащая объекты всех авторов.
# Имеет следующие поля:
# 	cвязь «один к одному» с встроенной моделью пользователей User;
# 	рейтинг пользователя. Ниже будет дано описание того, как этот рейтинг можно посчитать.
class Author(models.Model): #User AbstractUser
    #fullname = models.CharField(max_length = 255)
    #rate = models.FloatField(default = 0.0)
    authorUser = models.OneToOneField(User, on_delete= models.CASCADE)
    ratingAuthor = models.SmallIntegerField(default=0)

    #def update_rating(self):
    #  postRat = self.post_set.aggregate(postRating = Sum('rating'))
    #  pRat = 0
    #  pRat += postRat.get('postRating')
    #  commentRat = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
    #  cRat = 0
    #   cRat += commentRat.get('rating') if commentRat else 0

    #   self.ratingAuthor = pRat *3 + cRat
    #   self.save()

    def update_rating(self): # с проверкой,не пустой ли рейтинг
        postRat = self.post_set.all() or 0
        if postRat:
            postRat = postRat.aggregate(rating=Sum('rating'))

        pRat = 0
        pRat += postRat.get('rating') if postRat else 0

        commentRat = self.user.comment_set.all() or 0
        if commentRat:
            commentRat = commentRat.aggregate(rating=Sum('rating'))

        cRat = 0
        cRat += commentRat.get('rating') if commentRat else 0

        self.rating = pRat * 3 + cRat
        self.save()



# 2.	Модель Category
# Категории новостей/статей — темы, которые они отражают (спорт, политика, образование и т. д.). Имеет единственное поле: название категории. Поле должно быть уникальным (в определении поля необходимо написать параметр unique = True).
class Category(models.Model):
    name = models.CharField(max_length=64, unique=True)



# 3.	Модель Post
# Эта модель должна содержать в себе статьи и новости, которые создают пользователи. Каждый объект может иметь одну или несколько категорий.
# Соответственно, модель должна включать следующие поля:
# 	связь «один ко многим» с моделью Author;
# 	поле с выбором — «статья» или «новость»;
# 	автоматически добавляемая дата и время создания;
# 	связь «многие ко многим» с моделью Category (с дополнительной моделью PostCategory);
# 	заголовок статьи/новости;
# 	текст статьи/новости;
# 	рейтинг статьи/новости.
class Post(models.Model):

    author = models.ForeignKey(Author, on_delete= models.CASCADE, verbose_name = "Автор")

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья')
    )
    categoryType = models.CharField(max_length=2, choices=CATEGORY_CHOICES, default=ARTICLE , verbose_name = "Категория")
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name = "Дата создания новости") # автоматически добавлять время создания поста
    postCategory = models.ManyToManyField(Category, through='PostCategory', verbose_name = "Тематика")
    title =  models.CharField(max_length=128, verbose_name = "Заголовок")
    text = models.TextField(verbose_name = "Текст")
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()


    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        #return '{}…{}'.format(self.text[0..123],'...')
        return self.text[0:123] + '...'

    def __str__(self):
        return f'{self.title.title()}: {self.text}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'


# 4.	Модель PostCategory
# Промежуточная модель для связи «многие ко многим»:
# 	связь «один ко многим» с моделью Post;
# 	связь «один ко многим» с моделью Category.
class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)
  #  _amount = models.IntegerField(default=1, db_column='amount')



# 5.	Модель Comment
# Под каждой новостью/статьёй можно оставлять комментарии, поэтому необходимо организовать их способ хранения тоже.
# Модель будет иметь следующие поля:
# 	связь «один ко многим» с моделью Post;
# 	связь «один ко многим» со встроенной моделью User (комментарии может оставить любой пользователь, необязательно автор);
# 	текст комментария;
# 	дата и время создания комментария;
# 	рейтинг комментария.
class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)  # автоматически добавлять время создания поста
    rating = models.SmallIntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

#python manage.py shell
#Импортируем модели:
#from news.models import *

#создаем юзеров:

# u1 = User.objects.create_user('Alyona', 'alyona@mail.ru', 'alyonapass')
# u2 = User.objects.create_user('Alisa', 'alisa@mail.ru', 'alisapass')

# Author.objects.create(authorUser = u1)
#Author.objects.create(authorUser = u2)
#Category.objects.create(name = 'IT')
#Category.objects.create(name = 'POLIT')
#Category.objects.create(name = 'SOC')
#Category.objects.create(name = 'HIST')

 #author = Author.objects.get(id = 1)

# Post.objects.create(author = author, categoryType = 'AR', title = 'sometitle', text = 'somebigtext')

#Post.objects.create(author=author, categoryType='AR', title='Руководство по проектированию реляционных баз данных', text='1. Вступление. Если вы собираетесь создавать собственные базы данных, то неплохо было бы придерживаться правил проектирования баз данных, так как это обеспечит долговременную целостность и простоту обслуживания ваших данных. Данное руководство расскажет вам что представляют из себя базы данных и как спроектировать базу данных, которая подчиняется правилам проектирования реляционных баз данных.Базы данных – это программы, которые позволяют сохранять и получать большие объемы связанной информации. Базы данных состоят из таблиц, которые содержат информацию. Когда вы создаете базу данных необходимо подумать о том, какие таблицы вам нужно создать и какие связи существуют между информацией в таблицах. Иначе говоря, вам нужно подумать о проекте вашей базы данных. Хороший проект базы данных, как было сказано ранее, обеспечит целостность данных и простоту их обслуживания.')

#Post.objects.get(id = 1).title
# присвоили статье категорию IT:
#Post.objects.get(id = 1).postCategory.add(Category.objects.get(id = 1))

#Post.objects.create(author = author, categoryType = 'AR', title = 'sometitle', text = 'somebigtext')

#Comment.objects.create(commentPost= Post.objects.get(id = 1), commentUser = Author.objects.get(id = 2).authorUser, text = 'Интересная статья, спасибо!')

#Comment.objects.get(id = 1).like()
#Comment.objects.get(id = 1).rating
#Post.objects.get(id = 1).like()
#Post.objects.get(id = 1).dislike()
#Post.objects.get(id = 1).dislike()
#Post.objects.get(id = 1).dislike()
#Post.objects.get(id = 1).rating



#Comment.objects.create(commentPost= Post.objects.get(id = 1), commentUser = Author.objects.get(id = 1).authorUser, text = 'Спасибо за отзыв!')
