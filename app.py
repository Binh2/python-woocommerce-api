from flask import Flask, render_template, redirect, url_for, request
from forms import ProductForm
import secrets
import sys
import api
import re


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_urlsafe(16)

def format_product_for_post(product: dict):
  print(f'{product["images"]=}')
  images = [ {"src": image } for image in product['images'].split(',') ]
  
  result = {
    'name': product['name'],
    'images': images,
    'description': f"<b>Brand: {product['brand']}</b>\n" + product['description'],
    'regular_price': product['price'],
  }
  try:
    result['id'] = product['id']
  except:
    pass
  return result

def format_product_for_display(product: dict):
  result = {
    'id': str(product['id']),
    'name': product['name'],
    'image': product['images'][0]['src'] if len(product['images']) > 0 else '',
    'images': [ image['src'] for image in product['images'] ] if len(product['images']) > 0 else [],
    'description': product['description'],
    'price': "{:,.0f}₫".format(float(product['sale_price'] if product['sale_price'] else product['regular_price'])),
  }
  return result

@app.route('/', defaults={"page": '1'})
@app.route('/?page=<page>', methods=['GET', 'POST'])
def products(page):
  products = api.get_products(page)
  products = [ format_product_for_display(product) for product in products ]
  return render_template('products.html', products=products)

@app.route('/products/<id>', methods=['GET', 'POST'])
def product(id: str):
  product = format_product_for_display(api.get_product(id))
  return render_template('product.html', product=product)

@app.route('/create', methods=['GET', 'POST'])
def create():
  print(request, file=sys.stderr)
  print(request.form, file=sys.stderr)
  form = ProductForm()
  return render_template('form.html', form=form, id=None, action="/api/create")

@app.route('/api/create', methods=['POST'])
def handle_create():
  product = format_product_for_post(dict(request.form))
  product = api.post_product(product)
  return redirect('/products/' + str(product['id']))

@app.route('/update/<id>', methods=['GET', 'POST'])
def update(id: str):
  product = api.get_product(id)
  form = ProductForm()
  form.name.data = product['name']
  form.description.data = product['description']
  form.price.data = product['sale_price'] if product['sale_price'] else product['regular_price']
  form.images.data = ','.join([ image['src'] for image in product['images'] ])
  return render_template('form.html', form=form, id=id, action="/api/update/" + id)

@app.route('/api/update/<id>', methods=['POST'])
def handle_update(id: str):
  product = dict(request.form)
  product['id'] = id
  product['brand'] = re.sub(r'(<p>)?<b>Brand: [\s\w]*<\/b>(<\/p>)?\n?', '', product['brand'])
  product = format_product_for_post(product)
  print(product)
  product = api.update_product(product)
  return redirect('/products/' + str(product['id']))

@app.route('/api/delete/<id>', methods=['GET', 'POST'])
def handle_delete(id: str):
  product = api.delete_product(int(id))
  print(f'{product=}')
  return redirect('/')

