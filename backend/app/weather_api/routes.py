from app import logger
from flask import jsonify, Response, request
from . import bp
import json


@bp.route('/')
@bp.route('/index')
def index():
    return jsonify({'welcome message': "Hi"})