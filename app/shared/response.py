# Built-in
import logging

# 3rd Party
from flask import jsonify

# Module
import error
from error import Errors
from app.config import config

logger = logging.getLogger(config.root_logger + __name__)

def jsonified(data, code=None):
    payload = {}
    if isinstance(data, Errors):
        payload['data'] = {'message': data.message,
                           'category': data.category}
        pass
    elif isinstance(data, (str, list, dict)):
        #return normal response
        payload['data'] = data
        payload['code'] = code or 200
    else:
        logger.error("jsonified accepts {types}".format(types=(str(type(Errors)), str(type(dict)), str(type(list)))))
        raise error.SystemError()


    return jsonify(payload), payload['code']