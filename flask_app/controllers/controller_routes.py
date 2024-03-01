from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.model_event import Event

# DISPLAY ROUTE -> Shows the form to create an event
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')