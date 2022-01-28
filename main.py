from flask import Flask
import logging as logger

from repository import Session

"""
    Main application
"""

flaskAppInstance = Flask(__name__)


if __name__ == '__main__':
    logger.debug("Main application starting..........")
    from controller import *
    flaskAppInstance.run(host="0.0.0.0", port=8080, debug=True)
    logger.info("Main application successfully started..!!!")