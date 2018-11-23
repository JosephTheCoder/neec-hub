from app import logger
from flask import jsonify, Response, request
from . import bp
from .handlers.agent_handler import AgentHandler
import json


@bp.route('/')
@bp.route('/index')
def index():
    return jsonify({'welcome message': "Hi, this is the ADA deflection API"})


#---------------------------------------------------------------
# def update_agent:
# Endpoint to start updating the Dialogflow Agent
# --------------------------------------------------------------
@bp.route('/update/<string:language>', methods=['GET'])
def update_agent(language):
    logger.info('Agent update started...')

    if language == 'all':
        logger.info("Updating every languages")
        AgentHandler.check_for_updates()
    else:
        logger.info("Updating language: %s", language)
        language = [language.decode("utf-8")]
        AgentHandler.check_for_updates(every_language=False, languages=language)



    return jsonify({'message': "Agent finished updating"})

