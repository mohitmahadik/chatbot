# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named Tele2Bot
T2Chat = ChatBot(
    'Tele2Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=['chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            # 'import_path': 'chatterbot.logic.SpecificResponseAdapter',
            'default_response': 'I did not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    read_only=True,
    database_uri='sqlite:///database.sqlite3'
)

trainer = ListTrainer(T2Chat)

trainer.train([
    "Hi",
    "Hello",
    "How are you?",
    "I am fine",
])
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
