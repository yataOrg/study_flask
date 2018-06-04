#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yata
# @Date:   2018-06-02 12:03:05
# @Last Modified by:   yata
# @Last Modified time: 2018-06-04 15:54:04

from flask import Flask, session, redirect, render_template, url_for, escape, request

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
	if request.method == 'POST':
		return render_template('index.html', app_content="afsafsafsafsaf")
	else return render_template('index.html', app_content="bbbbbbbbbbb")
	# body_data = pymysql.fetchall()


def factory(name = 'index'):
	return render_template(name)

	


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

if __name__ == '__main__':
	app.run(host='0.0.0.0')



