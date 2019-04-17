from flask_restful import Resource, reqparse
from repositories.DatabaseHandler import *
from models.UserModel import User


class UsersController(Resource):
    def get(self):
        user_result = get_users()

        users = []

        for res in user_result:
            users.append(User(res).serialize())

        return {'message': 'Success', 'data': users}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('email', required=True)

        # Parser arguments into obj
        args = parser.parse_args()

        user = (args['firstName'], args['lastName'], args['email'])
        new_user = {'id': add_user(user)}

        if new_user['id'] is None:
            return {'message': 'Email Already Exists', 'data': args}, 409

        new_user.update(args)

        return {'message': 'User created', 'data': new_user}, 201
