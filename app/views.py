from django.shortcuts import render
from django.http import JsonResponse
import json
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from django.views import View
from chatapp.settings import CHATTERBOT
from .models import Chat



def index(request):
    return render(request, 'index.html')



class ChatterBotApiView(View):
    """
    Provide an API endpoint to interact with ChatterBot.
    """

    chatterbot = ChatBot(**CHATTERBOT)

    
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