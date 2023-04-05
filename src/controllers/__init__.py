from flask import Blueprint

bp = Blueprint('spaceship', __name__)

from . import spaceship
