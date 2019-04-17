from flask_restful import Resource, reqparse
from repositories.DatabaseHandler import *
from models.UserNoteModel import UserNotes
from models.UserModel import User
from services.PauliusNoteService import PauliusNoteService


class UserNoteController(Resource):
    def get(self, user_id):
        if not self.id_valid(user_id):
            return {'message': 'User not found', 'data': {}}, 404

        notes = PauliusNoteService().get_all_notes()

        user_result = get_user(user_id)
        user = User(user_result)
        user_notes_results = get_user_notes(user_id)
        user_notes = []

        for note in notes:
            for res in user_notes_results:
                if note.title == res[2]:
                    user_notes.append(note)

        return {'message': 'User notes', 'data': UserNotes(user, user_notes).serialize()}, 200


    def id_valid(self,id):
        user_results = get_users()

        for res in user_results:
            if res[0] == id:
                return True

        return False