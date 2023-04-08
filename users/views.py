from django.contrib import messages
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import CreateView

from users.decorators import user_not_authenticated
from users.forms import RegisterUserForm, LoginUserForm, SetPasswordForm, PasswordResetForm
from users.services import RegistrationServices
from users.tokens import account_activation_token

services = RegistrationServices()

# Главная страница
def index(request):
    return render(request, 'users/home.html')

def index_id(request, id):
    return HttpResponse(id)

# Активация аккаунта
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True   # активировать пользователя
        user.save()

        messages.success(request, "Почта успешно подтверждена")
        return redirect('login')
    else:
        messages.error(request, "Нерабочая ссылка!")

    return redirect('home')

# 404
def pageNotFound(request, exception):
	return HttpResponseNotFound('page does not exist')

# Регистрация
@user_not_authenticated
def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)   # форма регистрации
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            user_email = form.cleaned_data.get('email')
            email_sent = services.activateEmail(request, user, user_email)   # отправка почты
            if email_sent:
                messages.success(request, f'На {user_email} была выслана ссылка на активацию \
                                            Пожалуйста активируйте аккаунт.')
            else:
                messages.error(request, f'Не получилось отправить ссылку активации на {user_email}, \
                                          Проверьте корректность введенной почты.')

            return redirect('home')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = RegisterUserForm()

    return render(
        request=request,
        template_name="users/register.html",
        context={"form": form}
        )

@user_not_authenticated
def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)   # форма - забыл пароль - пользователь вводит почту
        if form.is_valid():
            user_email = form.cleaned_data['email']
            email_sent = services.resetPassword(request, user_email)   # отправка почты

            if email_sent:
                messages.success(request,
                    f"""
                    На вашу почту {user_email} была выслана инструкция для смены пароля.
                    Пожалуйста перейдите в письмо и пройдитесь по дальнейшей инструкции для смены пароля.
                    """
                )
            else:
                messages.error(request, f"Проблемы с отправкой письма на почту {user_email}")

            return redirect('home')

    form = PasswordResetForm()
    return render(
        request=request,
        template_name="users/password_reset_request.html",
        context={"form": form}
        )

@login_required
def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)   # форма на смену пароля
        if form.is_valid():
            form.save()
            messages.success(request, "Пароль успешно изменен")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'users/password_reset_confirm.html', {'form': form})

# Пользователь переходит по данной ссылке для смены пароля
def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)   # форма на смену пароля
            if form.is_valid():
                form.save()
                messages.success(request, "Пароль был успешно изменен.")
                return redirect('login')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'users/password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Ссылка недействительна")

    messages.error(request, 'Что-то пошло не так.')
    return redirect("home")

# Вход
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('home')   # перенапраление на главную страницу

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Вы вышли с аккаунта.")
    return redirect("home")