# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import db
from datetime import datetime

# model the class after the game table from our database
class Calendar:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # add additional columns here
        self.name = data['name']
        self.location = data['location']
        self.description = data['description']
        self.calendar_date = data['calendar_date']
        self.calendar_time = data['calendar_time']
        self.user_id = data['user_id']
    
    # CREATE
    @classmethod
    def create(cls, data:dict):
        #! # TODO change calendars to the table name and update the column names and values
        query = "INSERT INTO calendars (name, location, description, calendar_date, calendar_time, user_id) VALUES (%(name)s, %(location)s, %(description)s, %(calendar_date)s, %(calendar_time)s, %(user_id)s);"
        id = connectToMySQL(db).query_db(query, data)
        return id

    # READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM calendars;"
        results = connectToMySQL(db).query_db(query)

        if not results:
            return []

        instance_list = []
        for dict in results:
            instance_list.append(cls(dict))
        return instance_list

    # READ ONE
    @classmethod
    def get_one_calendar(cls, data:dict):
        #! #TODO change calendars to the table name
        query = "SELECT * FROM calendars WHERE id = %(id)s;"
        results = connectToMySQL(db).query_db(query, data)

        if not results:
            return []

        #convert the first item in the list to an instance of the class
        dict = results[0]
        instance = cls(dict)
        return instance

    # UPDATE

    # DELETE
    @classmethod
    def delete_one(cls, data:dict):
        #! #TODO change calendars to the table name
        query = "DELETE FROM calendars WHERE id = %(id)s;"

    # READ BY YEAR AND MONTH
    @classmethod
    def get_by_year_and_month(cls, year: int, month: int):
        # Construct the start and end dates for the given month
        start_date = datetime(year, month, 1)
        if month == 12:
            end_date = datetime(year + 1, 1, 1)
        else:
            end_date = datetime(year, month + 1, 1)

        # Construct the query to retrieve events for the given month
        query = "SELECT * FROM calendars WHERE calendar_date >= %(start_date)s AND calendar_date < %(end_date)s;"
        data = {
            'start_date': start_date,
            'end_date': end_date
        }
        results = connectToMySQL(db).query_db(query, data)

        if not results:
            return []

        # Convert the results to instances of the Calendar class
        instance_list = []
        for row in results:
            instance_list.append(cls(row))
        return instance_list
