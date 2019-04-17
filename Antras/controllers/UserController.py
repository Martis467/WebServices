from flask_restful import Resource, reqparse
from repositories.DatabaseHandler import *
from models.UserModel import User


class UserController(Resource):
    def get(self, id):
        if not self.id_valid(id):
            return {'message': 'User not found', 'data': {}}, 404

        user_result = get_user(id)
        user = User(user_result)

        return {'message': 'User', 'data': user.serialize()}, 200

    def put(self, id):
        if not self.id_valid(id):
            return {'message': 'User not found', 'data': {}}, 404

        parser = reqparse.RequestParser()

        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('email', required=True)

        # Parser arguments into obj
        args = parser.parse_args()

        last_row = update_user((args['firstName'], args['lastName'], args['email']), id)

        if last_row is None:
            return {'message': 'Email Already Exists', 'data': {}}, 409

        updated_user = {'id': id}
        updated_user.update(args)

        return {'message': 'User updated successfully', 'data': updated_user}, 202

    def delete(self, id):
        if not self.id_valid(id):
            return {'message': 'User not found', 'data': {}}, 404

        delete_user(id)

        return '', 204

    def id_valid(self,id):
        user_results = get_users()

        for res in user_results:
            if res[0] == id:
                return True

        return False
