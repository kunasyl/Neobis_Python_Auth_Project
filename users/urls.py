from django.urls import path

from users.views import *

urlpatterns = [
    path('', index, name='home'),   # Главная страница
    path('<int:id>/', index_id),
    path('register/', RegisterUser.as_view(), name='register'),   # Регистрация
    path('login/', LoginUser.as_view(), name='login'),   # Авторизация
]

handler404 = pageNotFound