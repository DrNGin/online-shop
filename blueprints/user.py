from flask import Blueprint
import models.users

app = Blueprint("user", __name__)


@app.route('/user')
def user():
    return "Hello! This is user page :)"

