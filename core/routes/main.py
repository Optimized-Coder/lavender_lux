from flask import Blueprint, render_template, redirect, request
from ..models import Recipe

import os

main = Blueprint('main', __name__)

@main.route('/')
def index():

    context = {
        'title': 'Home | Lavender lux'
    }

    return render_template(
        'index.html',
        **context
    )

@main.route('/about/')
def about():
    context = {
        'title': 'About | Lavender lux'
    }
    return render_template(
        'about.html',
        **context
    )

@main.route('/recipes/discover/')
def discover():
    context = {
        'title': 'Discover | Lavender lux',
        'recipes': Recipe.query.all()
    }
    return render_template(
      'recipes.html',
        **context
    )

import stripe


DOMAIN = 'http://127.0.0.1:5000'

stripe.api_key = os.environ.get('STRIPE_API_KEY')

@main.route('/create-checkout-session/', methods=['GET', 'POST'])
def create_checkout_session():
    try:
        checkout_session = stripe.checkout.Session.create(
            line_items = [
                {
                    'price': 'price_1Nsd7BGp9TbKJ1EQyxPEhzsW',
                    'quantity': request.form.get('quantity'),
                },
            ],
            mode = 'payment',
            success_url = DOMAIN + '/success',
            cancel_url = DOMAIN + '/cancel',
        )
    except Exception as e:
        return str(e)
    return redirect(checkout_session.url, code=303)

@main.route('/success', methods=['GET', 'POST'])
def success():
    return render_template('product/success.html')

@main.route('/cancel', methods=['GET', 'POST'])
def cancel():
    return render_template('product/cancel.html')