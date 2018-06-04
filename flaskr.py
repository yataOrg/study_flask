#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: yata
# @Date:   2018-06-04 16:08:45
# @Last Modified by:   yata
# @Last Modified time: 2018-06-04 18:31:41

import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

def connect_db():
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv

def get_db():
	if not hasattr(g, 'sqlite_db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db

@app.teardown_appcontext
def close_db():
	if hasattr(g, 'sqlite_db'):
		g.sqlite_db.close()



if __name__ == '__main__':
	app.run()

