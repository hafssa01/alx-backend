#!/usr/bin/env python3
"""
Get locale from request
"""

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    """
    Configuration class for the Flask application.
    """ 
    LANGUAGES = ["en", "fr"] 
    BABEL_DEFAULT_LOCALE = "en" 
    BABEL_DEFAULT_TIMEZONE = "UTC"

app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)

@babel.localeselector
def get_locale():
    """
    This function determines the best match for the user's preferred language from the supported languages using the request's Accept-Language header.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """
    This function renders the 2-index.html template.
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run(debug=True)