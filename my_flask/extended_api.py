from my_flask.general import hi
import shortuuid
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
app.add_url_rule('/hoho', view_func=hi)

@app.route("/hi1")
def hello1():
    return "Hello !!!!!"

if __name__ == '__main__':
    app.run()