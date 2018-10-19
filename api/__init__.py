from flask import Flask

"""
Create a Flask application named sm.
sm  will be my flask instianted variable.
"""

sm = Flask(__name__)

from api import routes
