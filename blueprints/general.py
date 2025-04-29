from flask import Blueprint

app = Blueprint("general", __name__)



@app.route('/')
def main():
    return "Hello! main page"


@app.route('/about')
def about_page():
    return "About Us Page"

