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

class UserList(Resource):

    def get(self):
        if (request.args.get('user_id', 1) is not None):
            user_id = request.args.get('user_id')
            if str(user_id) in USER_LIST.keys():
                return USER_LIST[user_id]
        return USER_LIST

    def post(self):
        user_id = int(max(USER_LIST.keys())) + 1
        user_id = '%i' % user_id
        USER_LIST[user_id] = {'name': request.form['name']}
        return USER_LIST[user_id]

api.add_resource(UserList, '/users')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)