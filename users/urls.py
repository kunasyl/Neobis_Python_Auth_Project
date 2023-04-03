from django.urls import path

from users.views import *

urlpatterns = [
    path('', index, name='home'),
    path('<int:id>/', index_id),
    path('register/', RegisterUser.as_view(), name='register'),
]

handler404 = pageNotFound