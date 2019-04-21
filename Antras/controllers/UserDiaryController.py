from flask_restful import Resource, reqparse
from repositories.DatabaseHandler import *
from models.UserNoteModel import UserNotes
from models.UserModel import User
from services.PauliusNoteService import PauliusNoteService


class UserNotesController(Resource):
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

    def post(self, user_id):
        if not self.id_valid(user_id):
            return {'message': 'User not found', 'data': {}}, 404

        user_result = get_user(user_id)
        user = User(user_result)

        parser = reqparse.RequestParser()

        parser.add_argument('title', required=True)
        parser.add_argument('comment', required=True)

        # Parser arguments into obj
        args = parser.parse_args()

        note = {'title': args['title'] + "*" + str(user_id),
                'author': f'{user.first_name} {user.last_name}',
                'comment': args['comment'],
                'expiration': '2020-12-02'}

        added = PauliusNoteService().add_new_note(note)

        if added:
            add_user_note((user_id, args['title'] + "*" + str(user_id)))
            return {'message': 'Success', 'data': args}, 200
        else:
            return {'message': 'A note with this title already exists', 'data': args}, 409

    def id_valid(self,id):
        user_results = get_users()

        for res in user_results:
            if res[0] == id:
                return True

        return False


class UserNoteController(Resource):
    def delete(self, user_id, title):
        if not self.id_valid(user_id):
            return {'message': 'User not found', 'data': {}}, 404

        deleted = PauliusNoteService().delete_note(title + "*" + str(user_id))

        if deleted:
            delete_user_note((user_id, title))
            return '', 204
        else:
            return {'message': 'Note not found', 'data': {}}, 404

    def put(self, user_id, title):
        if not self.id_valid(user_id):
            return {'message': 'User not found', 'data': {}}, 404

        user_result = get_user(user_id)
        user = User(user_result)

        parser = reqparse.RequestParser()

        parser.add_argument('title', required=True)
        parser.add_argument('comment', required=True)

        # Parser arguments into obj
        args = parser.parse_args()

        note = {'title': args['title'] + "*" + str(user_id),
                'author': f'{user.first_name} {user.last_name}',
                'comment': args['comment'],
                'expiration': '2020-12-02'}

        updated = PauliusNoteService().update_note(title + "*" + str(user_id), note)

        if updated == 202:
            new_title = args['title'] + "*" + str(user_id)
            old_title = title + "*" + str(user_id)
            update_user_note(old_title, new_title)
            return {'message': 'Success', 'data': args}, 200
        if updated == 409:
            return {'message': 'A note with this title already exists', 'data': args}, 404
        if updated == 404:
            return {'message': 'Note not found', 'data': {}}, 404


    def id_valid(self, id):
        user_results = get_users()

        for res in user_results:
            if res[0] == id:
                return True

        return False
