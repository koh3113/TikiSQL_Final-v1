from flask import Flask, render_template, redirect, url_for
import requests
import sqlalchemy
import sql
app = Flask(__name__)


@app.route('/')
def index():
    categories = sql.get_categories()
    return render_template('index.html', categories=categories)

@app.route('/sub_category/<cat_id>')
def sub_category(cat_id):
    cat_id = int(cat_id)
    sub_category = sql.get_sub_cate(cat_id)
    if len(sub_category) == 0:
        return redirect(url_for('product',cat_id=cat_id))
    return render_template('subca.html', sub_category = sub_category)
        
@app.route('/product/<cat_id>')   
def product(cat_id):
    print(type(cat_id), cat_id)
    cat_id = int(cat_id)
    product = sql.get_product(cat_id)
    return render_template('product.html', product = product)
    

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)