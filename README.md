# newsp1
 учебный проект по созданию новостного портала на джанго
 
 Итоговый проект по разделу D4

1. Усовершенствовать ваш новостной портал. Добавить постраничный вывод 
https://github.com/alyonarud/newsp1/blob/main/NewsP/templates/news.html
и отдельную страницу с поиском /search/, 
https://github.com/alyonarud/newsp1/blob/main/NewsP/templates/search.html
чтобы пользователь мог сортировать новости по дате и имени автора.


2. Необходимо иметь возможность создавать новые новости и статьи не только из админки, но и в самом приложении. Для такой возможности необходимо создать модельные формы.
https://github.com/alyonarud/newsp1/blob/main/NewsP/news/forms.py

3. Необходимо добавить на сайт с помощью дженериков новые страницы /news/add/, а также /news/<int:pk>/edit/. На этих страницах пользователь может добавить или редактировать новости.
https://github.com/alyonarud/newsp1/blob/main/NewsP/news/views.py
https://github.com/alyonarud/newsp1/blob/main/NewsP/news/urls.py
https://github.com/alyonarud/newsp1/blob/main/NewsP/templates/post_create.html


4. Добавьте страницу удаления новостей /news/<int:pk>/delete/. На ней после подтверждения пользователь может удалить страницу с новостью.
 https://github.com/alyonarud/newsp1/blob/main/NewsP/templates/post_delete.html
 
===================================================

Итоговый проект по разделу D3

В результате работы с модулем вы должны были выполнить следующие задания:

1.Сделать новую страничку с адресом /news/, на которой должен выводиться список всех новостей.
https://github.com/alyonarud/newsp1/blob/main/NewsP/templates/news.html

2.Все cтатьи выведены в виде заголовка, даты публикации и первых 50 символов текста статьи.

3.Новости должны выводиться в порядке от более свежей до самой старой.
https://github.com/alyonarud/newsp1/blob/main/NewsP/news/views.py

Отображается всё по адресу /news/.
 
https://github.com/alyonarud/newsp1/blob/main/NewsP/news/urls.py


4.Сделать отдельную страницу для полной информации о статье /news/<id новости>. На этой странице должна быть вся информация о статье. Название, текст и дата загрузки в формате ДЕНЬ-МЕСЯЦ-ГОД ЧАС:МИНУТЫ.

https://github.com/alyonarud/newsp1/blob/main/NewsP/templates/post.html

5. Написать собственный фильтр Censor, который цензурирует нежелательную лексику в названиях и текстах статей.
см https://github.com/alyonarud/newsp1/blob/main/NewsP/news/templatetags/my_filters.py

Все новые странички должны быть частью основного шаблона default.html.


помимо этого:
1. добавлен вывод комментариев к посту

https://github.com/alyonarud/newsp1/blob/main/NewsP/templates/post.html

2. список цензурируемых слов загружается из внешнего файла censor_list.txt

см https://github.com/alyonarud/newsp1/blob/main/NewsP/news/templatetags/my_filters.py

