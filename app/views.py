from app import app
from flask import render_template
from .request import get_movies


@app.route("/")
def index():
    """

    define view for root page

    """
    # Getting popular movie
    popular_movies = get_movies('popular')
    print(popular_movies)
    title = 'Home - Welcome to The best Movie Review Website Online'
    return render_template('index.html', title=title, popular=popular_movies)
