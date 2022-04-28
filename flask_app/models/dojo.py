import imp
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db ="dojo_survey"

class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    @staticmethod
    def validate_form(form_data):
        is_valid = True
        if len(form_data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if not form_data['dojo_location']:
            flash("You must choose a location.")
            is_valid = False
        if not form_data['favorite_language']:
            flash("You must choose a language.")
            is_valid = False
        if len(form_data['comment']) < 3:
            flash("Comment must be at least 3 characters.")
            is_valid = False
        return is_valid
    @classmethod
    def get_one(cls, id):
        query  = "SELECT * FROM dojos WHERE id = %(id)s;"
        result = connectToMySQL(db).query_db(query, {'id':id})
        print(result)
        return cls(result[0])
    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL(db).query_db( query, data )  
    # # @classmethod
    # # def update(cls, data, id):
    # #     query = f"UPDATE dojos SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id = {id};"
    # #     return connectToMySQL(db).query_db(query,data)
    # # @classmethod
    # # def delete(cls, id):
    # #     query  = f"DELETE FROM dojos WHERE id = {id};"
    # #     return connectToMySQL(db).query_db(query)
    # # @classmethod
    # # def get_one_dojo_with_ninjas(cls, id):
    # #     query = f"SELECT * FROM dojos_and_ninjas_schema.ninjas LEFT JOIN dojos on dojo_id = dojos.id WHERE dojos.id = {id};"
    # #     results = connectToMySQL(db).query_db(query)
    # #     oneDojo = cls(results[0])
    # #     for row in results:
    # #         data = {
    # #             "id": row['id'],
    # #             "first_name": row['first_name'],
    # #             "last_name": row ['last_name'],
    # #             "age": row['age'],
    # #             "dojo_id": row['id'],
    # #             "created_at": row['created_at'],
    # #             "updated_at": row['updated_at'],
    # #         }
    # #         oneDojo.ninja_list.append(Ninja(data))
    # #     print(oneDojo.ninja_list)
    #     return oneDojo