#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, request
from flask.ext.restful import Api, Resource

app = Flask(__name__)
api = Api(app)

USER_LIST = {
    '1': {'name': 'Michael'},
    '2': {'name': 'Tom'}
}


class User(Resource):
    
    def get(self, user_id):
        return USER_LIST['user_id']

    def delete(self, user_id):
        del USER_LIST[user_id]
        return ''

    def put(self, user_id):
        USER_LIST[user_id] = {'name': request.form['name']}
        return USER_LIST[user_id]


api.add_resource(User, '/users/<user_id>')
app.run(host='0.0.0.0', debug=True)