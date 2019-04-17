from flask import Flask
from flask_restful import Api
import markdown
from controllers.UsersController import UsersController
from controllers.UserController import UserController
from controllers.UsersNotesController import UsersNotesController
from controllers.UserNotesController import UserNoteController

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    """Api documentation"""
    with open('README.md', 'r') as markdown_file:
        # Read file and convert it to HTML
        content = markdown_file.read()

        return markdown.markdown(content)


api.add_resource(UsersController, '/users')
api.add_resource(UserController, '/users/<int:id>')
api.add_resource(UsersNotesController, '/users/notes')
api.add_resource(UserNoteController, '/users/<int:user_id>/notes')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
