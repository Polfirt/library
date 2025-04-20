from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import CustomUserCreationForm, BookForm


def register(request):
    # Обработка регистрации пользователей
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! Please log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'library/register.html', {'form': form})


@login_required # Требует авторизации
def profile(request):
    # Показ профиля пользователя с его книгами
    books = Book.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'library/profile.html', {'books': books})


def book_list(request):
    # Список всех книг с фильтрацией по автору
    books = Book.objects.all().order_by('-created_at')
    author_filter = request.GET.get('author')

    if author_filter:
        books = books.filter(author__icontains=author_filter)

    return render(request, 'library/book_list.html', {
        'books': books,
        'author_filter': author_filter
    })


def book_detail(request, pk):
    # Детальная страница книги
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})


@login_required
def add_book(request):
    # Добавление новой книги
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            book = form.save(commit=False)
            book.user = request.user
            book.save()
            messages.success(request, 'Book added successfully!')
            return redirect('profile')
    else:
        form = BookForm()
    return render(request, 'library/book_form.html', {'form': form})


@login_required
def edit_book(request, pk):
    # Редактирование существующей книги
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_detail', pk=book.pk)
    else:
        form = BookForm(instance=book)
    return render(request, 'library/book_form.html', {'form': form})


@login_required
def delete_book(request, pk):
    # Удаление книги
    book = get_object_or_404(Book, pk=pk, user=request.user)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('profile')
    return render(request, 'library/book_confirm_delete.html', {'book': book})
