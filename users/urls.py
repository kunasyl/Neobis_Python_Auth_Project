from django.urls import path

from users.views import *

urlpatterns = [
    path('', index, name='home'),   # Главная страница
    path('<int:id>/', index_id),
    path('register/', register, name='register'),   # Registration
    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('login/', LoginUser.as_view(), name='login'),   # Авторизация
    path('reset/<uidb64>/<token>', passwordResetConfirm, name='password_reset_confirm'),
    path('logout/', custom_logout, name='logout'),
    path("password_change", password_change, name="password_change"),
    path("password_reset", password_reset_request, name="password_reset"),
]

handler404 = pageNotFound