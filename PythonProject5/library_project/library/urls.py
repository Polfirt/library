from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Регистрация
    path('register/', views.register, name='register'),
    # Стандартные представления аутентификации
    path('login/', auth_views.LoginView.as_view(
        template_name='library/login.html',
        extra_context={'title': 'Login'}
    ), name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='library/logout.html'
    ), name='logout'),

    # Профиль пользователя
    path('profile/', views.profile, name='profile'),

    # Работа с книгами
    path('', views.book_list, name='book_list'),
    path('book/add/', views.add_book, name='add_book'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('book/<int:pk>/edit/', views.edit_book, name='edit_book'),
    path('book/<int:pk>/delete/', views.delete_book, name='delete_book'),
]
# Обработка медиафайлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
