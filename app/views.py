from app import app
from flask import render_template

@app.route("/")
def index():
    """

    define view for root page

    """
    message = "hello Boyd"
    return render_template('index.html', message=message)