from django.db import models


class Articles(models.Model):
    title = models.CharField('Название', max_length=75, default='я забыл(')
    anons = models.CharField('Анонс', max_length=150, default='я забыл(')
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации статьи')

    def __str__(self):
        return f'Новость: {self.title}'


    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
