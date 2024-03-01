from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.model_user import User

# DISPLAY ROUTE -> Shows the form to create an users
@app.post('/users/login/process')
def users_login():
    return redirect('/dashboard')

# ACTION ROUTE -> Process the form from the new route (above) 
@app.post('/users/create')
def users_create():
    #TODO do the logic for creating the row in the database here
    return redirect('/dashboard')

# DISPLAY ROUTE -> Just display the users info
@app.route('/users/<int:id>')
def users_show(id):
    # TODO get the users from the database and pass that instance of the users to the html page
    return render_template('users_show.html')

# DISPLAY ROUTE -> Display the form to edit the users
@app.route('/users/<int:id>/edit')
def users_edit(id):
    #! # TODO in the future make sure that the user is supposed to be able to update the record
    # TODO get the users from the database and pass that instance of the users to the html page
    return render_template('users_edit.html')

# ACTION ROUTE -> Process the form from the edit route
@app.post('/users/<int:id>/update')
def users_update(id):
    #! # TODO in the future make sure that the user is supposed to be able to update the record
    # TODO using the id that comes in update the record
    return redirect('/')

# ACTION ROUTE -> Delete the record from the database
@app.post('/users/<int:id>/delete')
def users_delete(id):
    #! # TODO in the future make sure that the user is supposed to be able to update the record
    # TODO call on the delete method from the class to delete the row in the database
    return redirect('/')
