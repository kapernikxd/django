from django.db import models



# Create your models here.

class Category(models.Model):
    '''Модель категорий'''

    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"






class Tag(models.Model):
    '''Модель тегов'''

    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Тег"
        verbose_name_plural = "Теги"




class Post(models.Model):
    '''Модель постов'''

    title = models.CharField("Заголовок", max_length=100)
    mini_text = models.TextField("Мини текст")
    text = models.TextField("Текст")
    created_date = models.DateTimeField("Дата создания", auto_now=True)
    slug = models.SlugField("url", max_length=100, unique=True)


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"



class Comment(models.Model):
    '''Модель комментариев'''

    text = models.TextField("Текст комментария")
    created_date = models.DateTimeField("Дата создания комментария", auto_now=True)
    moderation = models.BooleanField(default=True)


    def __str__(self):
        return self.text


    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"