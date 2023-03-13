from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/chatbot/', views.ChatterBotApiView.as_view(), name='api'),
    path('home.html', views.home, name="home"),
    path('learn.html', views.learn, name="learn"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('login.html', views.login, name="login"),
    path('signup.html', views.signup, name="signup"),
]
