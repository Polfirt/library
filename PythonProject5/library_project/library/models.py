from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Book(models.Model):
    # Связь с пользователем: каждая книга принадлежит одному пользователю
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Название книги с максимальной длиной 200 символов
    title = models.CharField(max_length=200)
    # Автор книги
    author = models.CharField(max_length=200)
    # Подробное описание книги
    description = models.TextField()
    # Дата публикации книги
    publication_date = models.DateField()
    # Обложка книги с загрузкой в папку covers/
    cover = models.ImageField(upload_to='covers/')
    # Автоматическая дата создания записи
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        # Строковое представление объекта
        return self.title

    def get_absolute_url(self):
        # URL для детальной страницы книги
        return reverse('book_detail', kwargs={'pk': self.pk})
