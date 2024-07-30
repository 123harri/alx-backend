#!/usr/bin/env python3
"""
A Flask application with internationalization (i18n) support using
Flask-Babel.

This application supports English and French languages and uses UTC as
the default timezone.
"""

from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    """
    Configuration class for Flask application.

    Attributes:
        LANGUAGES (list): Supported languages for the application.
        BABEL_DEFAULT_LOCALE (str): Default locale for the application.
        BABEL_DEFAULT_TIMEZONE (str): Default timezone for the application.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match language for the request.

    The function first checks if a 'locale' parameter is provided in the
    URL query string. If so, it returns that locale if it's supported.
    Otherwise, it uses the best match from the Accept-Language HTTP header.

    Returns:
        str: The locale identifier that best matches the request.
    """
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/", methods=["GET"], strict_slashes=False)
def home() -> str:
    """
    Renders the home page.

    The function renders the '4-index.html' template.

    Returns:
        str: The rendered HTML template.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
