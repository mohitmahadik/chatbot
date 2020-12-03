from chatterbot.trainers import ListTrainer
from ChatBot import T2Chat
from flask import Flask, render_template, request



app = Flask(__name__)
app.static_folder = 'static'

@app.route("/")
def home():
    return render_template("Index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(T2Chat.get_response(userText))

if __name__ == "__main__":
    app.run()