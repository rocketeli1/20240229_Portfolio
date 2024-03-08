from flask import Flask, jsonify, render_template, redirect, request, session
from flask_app import app
from flask_app.models.model_calendar import Calendar
from flask_app.models.model_user import User

@app.route('/calendar')
def calendar():
    events = Calendar.get_all()
    return render_template('calendar.html', events=events)

@app.route('/calendar/add_event')
def calendarAddEvent():
    if 'uuid' not in session:
        return redirect('/users/login')
    return render_template('calendar_add_event.html')

@app.post('/calendar/add_event')
def calendarProcessAddEvent():
    if 'uuid' not in session:
        return redirect('/users/login')
    data = {
        **request.form,
        'user_id': session['uuid']
    }
    Calendar.create(data)
    return redirect('/calendar')

# Get events from MySQL
@app.route('/events', methods=['GET'])
def get_events():
    year = request.args.get('year')
    month = request.args.get('month')

    # Convert year and month to integers
    year = int(year)
    month = int(month)

    # Filter events based on the requested year and month
    events = Calendar.get_by_year_and_month(year, month)
    # Serialize events data to dictionary
    serialized_events = [{
        'name': event.name,
        'user_id': event.user_id,
        'calendar_date': event.calendar_date.strftime('%Y-%m-%d')  # Convert datetime object to string
    } for event in events]

    return jsonify(serialized_events)

@app.route('/calendar/<int:id>/edit')
def calendar_edit(id):
    one_calendar = Calendar.get_one_calendar({'id':id})
    loggedin_user = User.get_one_user({'id': session['uuid']})
    return render_template('edit_calendar.html', one_calendar=one_calendar, loggedin_user=loggedin_user)

@app.route('/calendar/<int:id>/delete')
def calendars_delete(id):
    if 'uuid' not in session:
        return redirect('/calendar')
    Calendar.delete_one(id)
    return redirect('/calendar')
