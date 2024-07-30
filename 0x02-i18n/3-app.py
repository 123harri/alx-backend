#!/usr/bin/env python3
"""A Basic Flask app with Babel for internationalization.
"""
from flask_babel import Babel, _
from flask import Flask, render_template, request


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
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
