from flask import Flask
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

"""
Create a Flask application named sm.
sm  will be my flask instianted variable.
"""

sm = Flask(__name__)
