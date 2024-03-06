from flask import Flask, render_template, redirect, request, session
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv
from flask_app import app
from flask_app.models.model_calendar import Calendar
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# Load environment variables from .env file
load_dotenv()

# Access environment variables
SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
RECEIVER_EMAIL = os.environ.get('RECEIVER_EMAIL')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

@app.route('/')          
def index():
    return render_template('index.html')

# other routes...
@app.route('/tableau')
def tableau():
    return render_template('tableau.html')

@app.route('/aboutMe')
def aboutMe():
    return render_template('aboutme.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

# contact form submission
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        date = request.form['date']

        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL
        msg['Subject'] = "New Contact Form Submission"

        body = f"Name: {name}\nEmail: {email}\nMessage: {message}\nDate: {date}"
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
        server.quit()

        return render_template('contact.html')

    return render_template('contact.html')
