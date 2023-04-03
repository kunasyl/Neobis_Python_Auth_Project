# import uuid
#
# from django.contrib.auth.base_user import BaseUserManager
# from django.contrib.auth.models import AbstractUser
from django.db import models
#
# class UserManager(BaseUserManager):
#
#     @staticmethod
#     def _validate_user(email: str):
#         if not email:
#             raise ValueError('Users must have an email address')
#
#     def create_user(self, email: str, password: str = None) -> 'User':
#         """
#         Creates and saves a User with the given email and phone number.
#         """
#         self._validate_user(email=email)
#
#         user = self.model(
#             email=self.normalize_email(email),
#             is_active=True,
#         )
#         # user.set_unusable_password()
#         user.set_password(password)
#         user.save()
#
#         return user
#
#     def create_superuser(self, email: str, password: str = None) -> 'User':
#         """
#         Creates and saves a superuser with the given email, phone number and password.
#         """
#         self._validate_user(email=email, password=None)
#
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#             is_active=True,
#             is_staff=True,
#             is_superuser=True
#         )
#         user.is_admin = True
#         # user.set_password(password)
#         user.save()
#
#         return user
#
#
# class User(AbstractUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4)
#     username = models.CharField(max_length=100, unique=True, verbose_name='Логин')
#     email = models.CharField(max_length=100, unique=True, verbose_name='Почта')
#     first_name = models.CharField(max_length=100, verbose_name='Имя')
#     last_name = models.CharField(max_length=100, verbose_name='Фамилия')
#     _password = models.CharField(max_length=100, verbose_name='Пароль')
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return f'{self.username}: {self.email}'
#
#     objects = UserManager()
#
#     EMAIL_FIELD = 'email'
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']