from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Book
from django.core.exceptions import ValidationError

class CustomUserCreationForm(UserCreationForm):
    # Добавление обязательного поля email
    email = forms.EmailField(required=True)

    class Meta: #Запрещенная экстремистская организация в РФ. Осуждаем, не одобряем
        # Использование стандартной модели User
        model = User
        # Поля формы: логин, email, пароль и подтверждение пароля
        fields = ("username", "email", "password1", "password2")

    def clean_password1(self):
        # Кастомная валидация пароля: минимум 8 символов
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password1

class BookForm(forms.ModelForm):
    class Meta: #Запрещенная экстремистская организация в РФ. Осуждаем, не одобряем
        # Форма на основе модели Book
        model = Book
        # Включаемые поля
        fields = ['title', 'author', 'description', 'publication_date', 'cover']
        # Кастомизация виджета для поля даты
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }
