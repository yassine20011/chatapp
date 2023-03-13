from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('api/chatbot/', views.ChatterBotApiView.as_view(), name='api'),
    path('home.html', views.home, name="home"),
    path('learn.html', views.learn, name="learn"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('bot.html', views.bot, name="bot"),
]
