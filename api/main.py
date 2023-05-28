from operator import itemgetter
import json
from woocommerce import API
import argparse

def init_wcapi():
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
    timeout=10,
  )
  return wcapi

def get_products():
  wcapi = init_wcapi()
  res = wcapi.get("products")
  return res.json()

  # # print(res.status_code)
  # # print(res.text)

def post_products(product: dict):
  wcapi = init_wcapi()
  req = wcapi.post("products", json.dumps(product))
  return req
  print(req.json())

if __name__ == '__main__':
  parser = argparse.ArgumentParser(prog='WooCommerce API', description='CRUD products', epilog='Bye bye')
  parser.add_argument('-a', '--action', choices=['c','r','u','d', ''], default='', nargs='?', help='To CRUD (Create/Read/Update/Delete) product')
  parser.add_argument('-i', '--id', help='Only apply for RUD (Read/Update/Delete)')
  args = parser.parse_args()
  
  if args.action == 'c':
    post_products({"name": "test"})
  elif args.action == 'r':
    print(get_products())
    

