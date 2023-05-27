from flask import Flask, render_template, redirect, url_for, request
from forms import ProductForm
import secrets
import sys


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)


@app.route('/', methods=('GET', 'POST'))
def index():
  form = ProductForm()
  return render_template('index.html', form=form)


@app.route('/handle_create', methods=('GET', 'POST'))
def handle_create():
  print(request, file=sys.stderr)
  print(request.form, file=sys.stderr)
  return redirect('/')

@app.route('/handle_read', methods=('GET', 'POST'))
def handle_read():
  # print(request, file=sys.stderr)
  print('hello', file=sys.stderr)
  return redirect('/')

@app.route('/handle_update', methods=('GET', 'POST'))
def handle_update():
  print(request, file=sys.stderr)
  print(request.form, file=sys.stderr)
  return redirect('/')

@app.route('/handle_delete', methods=('GET', 'POST'))
def handle_delete():
  print(request, file=sys.stderr)
  print(request.form, file=sys.stderr)
  return redirect('/')