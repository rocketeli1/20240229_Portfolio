from flask import Flask, render_template, redirect, request
from flask_bcrypt import Bcrypt
app = Flask(__name__, static_url_path='/static')
app.secret_key = "secret"

bcrypt = Bcrypt(app)

db = "20240228_portfolio"