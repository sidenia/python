from flask import Flask
from flask_restplus import Api

from src.server.instance import server

app, api = server.app, server.api

# poderia fazer uma request para um bd mas vamos fazer uma listagem aqui

books_db = [
    {'id': 0, 'title': 'O Pequeno Príncipe'},
    {'id': 0, 'title': 'Poliana'},
]


#endpoint /books
@api.route('/books')
class BookList():
    def get(self,):
        return books_db
