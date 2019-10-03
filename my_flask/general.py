import shortuuid
from flask import Flask
from flask_cors import CORS

from flask_httpauth import HTTPBasicAuth

def hello():
    return "Hello %s!!!!!"

def hi():
    return 'HELLO WORLD'