#!/usr/bin/env python3
"""A Flask app with Babel for internationalization and user emulation.
"""
from flask_babel import Babel, _
from flask import Flask, render_template, request, g


class Config:
    """Configuration class for Flask Babel.

    This class sets the available languages, default locale, and default
    timezone for the Flask application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Retrieve a user by their ID.

    This function returns a user dictionary or None if the ID cannot be
    found or if login_as was not passed.
    """
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None


@app.before_request
def before_request():
    """Run before each request.

    This function sets a user as a global variable if logged in.
    """
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """Determine the best match for supported languages.

    This function uses the Accept-Language header from the request to
    determine the best matching language from the supported languages.
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """Render the home/index page.

    This route renders the index.html template for the root URL.
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
