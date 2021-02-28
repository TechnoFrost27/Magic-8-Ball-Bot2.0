from flask import Flask
from threading import Thread
from functools import partial
app = Flask('')
@app.route('/')
def main():
    return "Your bot is alive!"
def run():
    Thread(target=partial(app.run,host="0.0.0.0")).start()