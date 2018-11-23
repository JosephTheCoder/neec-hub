from flask import Blueprint

bp = Blueprint('weather_api', __name__)

from app.weather_api import routes
