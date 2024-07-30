#!/usr/bin/env python3
"""
This module sets up a basic Flask application.
"""

from flask import Flask, render_template

app: Flask = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index() -> str:
    """
    This function renders the index.html template
    at the root URL.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
