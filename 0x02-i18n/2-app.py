#!/usr/bin/env python3
"""
This module sets up a basic Flask application
with Babel for internationalization.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Config class to set available languages,
    default locale, and timezone.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app: Flask = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel: Babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Determines the best match for supported
    languages using request.accept_languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Renders the index.html template at the root URL.
    """
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
