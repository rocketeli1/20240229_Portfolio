from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models.model_user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/users/login')
def usersLogin():
    return render_template('login_page.html')

# ACTION ROUTE - Processes the user's login info 
@app.post('/users/login/process')
def users_login():
    if User.validate_login(request.form) == False:
        print('is false')
        return redirect('/users/login')
    return redirect('/calendar') # Redirect to dashboard if login is successful


# ACTION ROUTE - Log the user out
@app.post('/users/logout')
def users_logout():
    del session['uuid']
    return redirect('/calendar')


# ACTION ROUTE - process the form from the new route (above)
@app.post('/users/register/process')
def users_create():
    # TO DO - do the logic for creating the row in the database here
    # Validate
    if User.validate_register(request.form) == False:
        return redirect('/users/login')
    # Set up hash
    hash_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password': hash_pw
    }
    # Create user
    id = User.create_user(data)
    # Store id into session
    session['uuid'] = id
    session['user_data'] = {
        'first_name': data['first_name'],
        'last_name': data['last_name'],
        'username': data['username'],
        'email': data['email']
    }
    return redirect('/calendar')


# DISPLAY ROUTE - just display the user info
@app.route('/users/<int:id>')
def users_show(id):
    #TO DO - get the user from the database and pass that instance of the user to the html page
    return render_template('user_show.html')


# DISPLAY ROUTE - display the form to edit the user
@app.route('/users/<int:id>/edit')
def users_edit(id):
    # TO DO - in the future make sure that the user is supposed to be able to update the record
    # TO DO - get the user from the database and pass that instance of the user to the html page
    return render_template('user_edit.html')


# ACTION ROUTE - process the form from the edit route (above)
@app.post('/users/<int:id>/update')
def users_update(id):
    # TO DO - in the future make sure that the user is supposed to be able to update the record
    # TO DO - using the id that comes in update the record
    return redirect('/calendar')


# ACTION ROUTE - delete the record from the database
@app.post('/users/<int:id>/delete')
def users_delete(id):
    # TO DO - in the future make sure that the user is supposed to be able to update the record
    # TO DO - call on the delete method from the class to delete the row in the database
    return redirect('/calendar')