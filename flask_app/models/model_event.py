# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import db

# model the class after the game table from our database
class Event:
    def __init__( self , data:dict ):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        # add additional columns here
        self.name = data['name']
        self.location = data['location']
        self.description = data['description']
        self.event_date = data['event_date']
        self.event_time = data['event_time']
        self.users_id = data['users_id']
    
    # CREATE
    @classmethod
    def create(cls, data:dict):
        #! # TODO change events to the table name and update the column names and values
        query = "INSERT INTO events (name, location, description, event_date, event_time, user_id) VALUES (%(name)s, %(location)s, %(description)s, %(event_date)s, %(event_time)s, %(user_id)s);"
        id = connectToMySQL(db).query_db(query, data)
        return id

    # READ ALL
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM events;"
        results = connectToMySQL(db).query_db(query)

        if not results:
            return []

        instance_list = []
        for dict in results:
            instance_list.append(cls(dict))
        return instance_list

    # READ ONE
    @classmethod
    def get_one(cls, data:dict):
        #! #TODO change events to the table name
        query = "SELECT * FROM events WHERE id = %(id)s;"
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
        #! #TODO change events to the table name
        query = "DELETE FROM events WHERE id = %(id)s;"
