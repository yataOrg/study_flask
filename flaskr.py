#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yata
# @Date:   2018-06-04 16:08:45
# @Last Modified by:   yata
# @Last Modified time: 2018-06-07 18:56:24

import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, _app_ctx_stack

# create our little application
app = Flask(__name__)
app.config.from_envvar('FLASK_SETTINGS', silent=True)

# print(app.config)
def connect_db():
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('entries.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()


def get_db():

	top = _app_ctx_stack.top
	if not hasattr(top, 'sqlite_db'):
		top.sqlite_db = connect_db()
	return top.sqlite_db


class InvalidUsage(Exception):
    status_code = 400
    def __init__(self, message, status_code):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

@app.errorhandler(InvalidUsage)
def invalid_usage(error):
    response = make_response(error.message)
    response.status_code = error.status_code
    return response

@app.route("/exception"):
def exception():
    raise InvalidUsage("No privilege to access the resource", status_code = 403)


@app.teardown_appcontext
def close_db(exception):
	top = _app_ctx_stack.top
	if hasattr(top, 'sqlite_db'):
		top.sqlite_db.close()


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select title, text from entries order by id desc ')
    entries = [dict(title=row[0], text=row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries = entries)



@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_id'):
        abort(401)
    db = get_db()
    db.execute('insert into entries (title, text) values (?, ?)',
               [request.form['title'], request.form['text']])
    db.commit()
    flash("New entry was successfully posted")
    return redirect(url_for('show_entries'))


@app.route("/login", methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_id'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error = error)

@app.route("/logout")
def logout():
    session.pop('logged_id', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
	init_db()
	app.run()

