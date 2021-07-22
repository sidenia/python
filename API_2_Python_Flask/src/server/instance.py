from flask import flask
from flask_restplus import Api


class Server():
    def __init__(self,):
        self.app = flask(__name__)
        self.app = Api(self.app,
                       version='1.0',
                       title='Sample Book API',
                       description='A simple book API',
                       doc='/docs')


def run(self,):
    self.app.run(
        debug=True
    )


server = Server()
