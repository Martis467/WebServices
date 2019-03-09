import shelve
from flask import Flask, g
from flask_restful import Resource, reqparse

app = Flask(__name__)


class UserList(Resource):
    def get(self):
        shelf = get_db()
        keys = list(shelf.keys())

        users = []

        for key in keys:
            users.append(shelf[key])

        return {'message': 'Success', 'data': users}, 200

    def post(self):
        parser = reqparse.RequestParser()

        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('email', required=True)

        # Parser arguments into obj
        args = parser.parse_args()

        shelf = get_db()
        shelf[args['email']] = args

        return {'message': 'User created', 'data': args}, 201


class Users(Resource):
    def get(self, email):
        shelf = get_db()

        if not (email in shelf):
            return {'message': 'User not found', 'data': {}}, 404

        return {'message': 'User', 'data': shelf[email]}, 200

    def put(self, email):
        shelf = get_db()

        if not (email in shelf):
            return {'message': 'User not found', 'data': {}}, 404

        parser = reqparse.RequestParser()

        parser.add_argument('firstName', required=True)
        parser.add_argument('lastName', required=True)
        parser.add_argument('email', required=True)

        # Parser arguments into obj
        args = parser.parse_args()

        shelf = get_db()
        shelf[email] = args

        return {'message': 'User updated successfully', 'data': args}, 202

    def delete(self, email):
        shelf = get_db()

        if not (email in shelf):
            return {'message': 'User not found', 'data': {}}, 404

        del shelf[email]

        return '', 204


def fill_start():
    shelf = get_db()
    test_user1 = \
        {
            'firstName': 'Seras',
            'lastName': 'Meras',
            'email': 'eskaferas@gmail.com'
        }
    test_user2 = \
        {
            'firstName': 'Oras',
            'lastName': 'Moras',
            'email': 'Soras@gmail.com'
        }

    if test_user1['email'] in shelf:
        return

    shelf[test_user1['email']] = test_user1
    shelf[test_user2['email']] = test_user2


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = shelve.open("users.db")
    return db


@app.teardown_appcontext
def teardown_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
