import psycopg2
from bs4 import BeautifulSoup

conn = psycopg2.connect(user='lenovo', database='coderschool', password='1')
conn.autocommit=True 
cursor = conn.cursor()

def get_categories():
    cursor.execute('SELECT name, cat_id FROM categories LIMIT 16')
    categories = cursor.fetchall()
    return categories

def get_sub_cate(cat_id):
    cursor.execute(f"SELECT name,cat_id FROM categories WHERE parent_id = %s;", (cat_id,))
    sub_cates = cursor.fetchall()
    return sub_cates    

def get_product(cat_id):
    cursor.execute(f"SELECT title, price, img_url FROM products2 WHERE category_id = %s LIMIT 20;", (cat_id,))
    products = cursor.fetchall()
    print(len(products))
    return products
  