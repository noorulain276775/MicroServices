from django.urls import path
from .views import RegisterUser, LoginView

urlpatterns = [
    path('register', RegisterUser.as_view()),
    path('login', LoginView.as_view()),
]
