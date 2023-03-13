from django.core.management.base import BaseCommand
from chatterbot import ChatBot
from chatterbot.ext.django_chatterbot import settings
from chatterbot.trainers import ListTrainer


class Command(BaseCommand):
    help = "Training the chatbot"

    def handle(self, *args, **options):
        conversations = []
        with open("dialogs.txt", "a+") as f:
            f.seek(0)
            data = f.read()
            data = data.split("\n")

            conversations = []
            for str in data:
                l = str.split("\t")
                conversations.extend((l[0], l[1]))

        chatterbot = ChatBot(**settings.CHATTERBOT)
        trainer = ListTrainer(chatterbot)
        trainer.train(
            [
                'Hi',
                'Hello there!',
                'Reda',
                'is one of my creators',
                'Tarik',
                'is one of my creators'
            ]
        )
        self.stdout.write(self.style.SUCCESS("Successfull!"))
