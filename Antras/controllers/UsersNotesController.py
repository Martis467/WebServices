# Flask
from flask_restful import Resource
# Repo
from repositories.DatabaseHandler import *
# models
from models.UserModel import User
from models.UserNoteModel import UserNotes
# Services
from services.PauliusNoteService import PauliusNoteService


class UsersNotesController(Resource):
    def get(self):
        user_result = get_users()

        users = [User(res) for res in user_result]
        notes = PauliusNoteService().get_all_notes()
        users_notes = []

        for user in users:
            note_results = get_user_notes(user.id)

            # if  paulius note title matches with user note table title, then add it to user_notes
            user_notes = []

            for note in notes:
                for res in note_results:
                    if note.title == res[2]:
                        user_notes.append(note)

            users_notes.append(UserNotes(user, user_notes).serialize())

        return {'message': 'Success', 'data': users_notes}, 200






