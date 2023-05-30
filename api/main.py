import sys
from operator import itemgetter
import json
from woocommerce import API
import argparse

def init_wcapi(timeout: int = 20):
  base_url = ''
  consumer_key = ''
  consumer_secret = ''

  with open("ini.json") as file:
    obj = json.load(file)
    base_url, consumer_key, consumer_secret = itemgetter('base_url', 'consumer_key', 'consumer_secret')(obj)

  wcapi = API(
    url=base_url,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    version="wc/v3",
    timeout=timeout,
  )
  return wcapi

def get_product(id: int):
  wcapi = init_wcapi()
  res = wcapi.get("products/"+str(id))
  return json.loads(res.text)

def get_products(page: int = 1, per_page: int = 20):
  wcapi = init_wcapi()
  res = wcapi.get("products", params={'per_page': per_page, 'page': page})
  return json.loads(res.text)

# def post_products(products: list[dict]):
#   wcapi = init_wcapi()
#   req = wcapi.post("products", json.dumps(products))
#   return json.loads(req.text)

def post_product(product: dict):
  wcapi = init_wcapi()
  req = wcapi.post("products", product)
  
  ERROR_CODE = 400
  if req.status_code >= ERROR_CODE:
    print(f'{req.status_code=}')
    print(f'{req.text=}', file=sys.stderr)
    raise ValueError('failed to post a product')
  
  return json.loads(req.text)

def update_product(product: dict, timeout: int = 60):
  id = str(product['id'])
  wcapi = init_wcapi(timeout)
  req = wcapi.put("products/" + str(id), product)
  ERROR_CODE = 400
  if req.status_code >= ERROR_CODE:
    print(f'{req.status_code=}')
    print(f'{req.text=}', file=sys.stderr)
    raise ValueError('failed to post a product')
  return json.loads(req.text)

def delete_product(id: int):
  wcapi = init_wcapi()
  req = wcapi.delete("products/" + str(id))
  return json.loads(req.text)

if __name__ == '__main__':
  from pprint import pprint
  parser = argparse.ArgumentParser(prog='WooCommerce API', description='CRUD products', epilog='Bye bye')
  parser.add_argument('-a', '--action', choices=['c','r','u','d', ''], default='', nargs='?', help='To CRUD (Create/Read/Update/Delete) product')
  parser.add_argument('-i', '--id', help='Only apply for RUD (Read/Update/Delete)')
  args = parser.parse_args()
  
  if args.action == 'c':
    print(post_product({
      "name": "test", 
      'images': [
        {'src': r'http://demo.woothemes.com/woocommerce/wp-content/uploads/sites/56/2013/06/T_2_front.jpg'}
      ],
      'regular_price': '245453',
      'sale_price': '245453',
    }))
  elif args.action == 'r':
    pprint(get_product(2288))
  elif args.action == 'u':
    pprint(update_product({'id': 2328, "name": "test2", "attributes": [{ 'name': 'Brand', "options": ["test3"]}]}))
  elif args.action == 'd':
    print(delete_product())
    

