from flask import Blueprint, render_template

product = Blueprint('product', __name__, url_prefix='/product')

@product.route('/')
def index():
    return render_template('product/index.html')