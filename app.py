import os
from chalice import Chalice
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

app = Chalice(app_name='serverless-chatterbot')
app.debug = True

chatbot = ChatBot(
    'fiobot',
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    database_uri=os.environ.get('DATABASE_URI')
)

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

chatbot.set_trainer(ListTrainer)
chatbot.train(conversation)


@app.route('/')
def index():
    text = app.current_request.query_params.get('text')
    response = chatbot.get_response(text)
    return {'reply': response.text}
