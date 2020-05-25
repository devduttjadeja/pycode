# 1) https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
# 2) https://flask.palletsprojects.com/en/1.1.x/tutorial/
# 3) https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
# 4) https://realpython.com/tutorials/flask/

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "This is an example app haha "

app.run()