from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/chatbot/', views.ChatterBotApiView.as_view(), name='api'),
    path('about/',views.about,name="room"),
]
