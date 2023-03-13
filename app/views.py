from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from django.views import View
from chatterbot.ext.django_chatterbot import settings
from django.contrib.auth.models import User
from .models import Chat


def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def learn(request):
    return render(request, 'learn.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("passwords don't match, please retype!!! ")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
        return redirect('login.html')

    return render(request, 'signup.html')


class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**settings.CHATTERBOT)

    def post(self, request, *args, **kwargs):
        """
        Return a response to the statement in the posted data.

        * The JSON data should contain a 'text' attribute.
        """
        input_data = request.POST['message']
        print(input_data)

        response = self.chatterbot.get_response(input_data)
        print(response)
        response_data = response.serialize()

        return JsonResponse(response_data, status=200)

    def get(self, request, *args, **kwargs):
        """
        Return data corresponding to the current conversation.
        """
        return JsonResponse({
            'name': self.chatterbot.name
        })
