from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

bot = ChatBot(
    'Terminal',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)


trainer = ListTrainer(bot)

conversations = [
    "Hello",
    "Hi there!",
    "How are you?",
    "I'm doing well, thank you.",
    "What's your name?",
    "My name is ChatterBot.",
    "How can I help you?",
    "Tell me a joke.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "That's hilarious!",
    "Glad you liked it!",
    "Bye",
    'It was nice talking to you.',
    'Thank you',
    'You are welcome.',
    'Goodbye'
    'Goodbye'
    'Hi'
    'Hello']

trainer.train(conversations)



print('Type something to begin...')

while True:
    try:
        user_input = input()
        if user_input == 'exit':
            break

        bot_response = bot.get_response(user_input)

        print(bot_response)

    # Press ctrl-c or ctrl-d on the keyboard to exit
    except (KeyboardInterrupt, EOFError, SystemExit):
        break