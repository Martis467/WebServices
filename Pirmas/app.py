from flask import Flask, g
from flask_restful import Api
import markdown

from User import UserList, User

app = Flask(__name__)
api = Api(app)


@app.route('/')
def index():
    """Api documentation"""

    with open('README.md', 'r') as markdown_file:
        # Read file and convert it to HTML
        content = markdown_file.read()

        return markdown.markdown(content)


api.add_resource(UserList, '/users')
api.add_resource(User, '/users/<string:email>')


if __name__ == '__main__':
    app.run()
