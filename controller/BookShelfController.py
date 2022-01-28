import json

from flask import Response
from flask_restful import Resource
import logging as logger

from model.BookShelf import BookShelf
from repository.BookShelfRepository import ShelfRepository

shelf_repository = ShelfRepository()


def response_success(myResponse, response_code=200):
    # create a dict  response object.
    result = {"code": response_code, "message": "successful", "payload": myResponse}
    return Response(json.dumps(result, sort_keys=True, indent=4),
                    response_code, mimetype='application/json')


def response_failure(myResponse, response_code=500):
    # create a dict  response object.
    result = {"code": response_code, "message": "Fail", "payload": myResponse}
    return Response(json.dumps(result, sort_keys=True, indent=4),
                    response_code, mimetype='application/json')


class ShelfSearchById(Resource):

    def get(self, id):
        logger.info("Fetching bookshelf with id {}".format(id))
        shelf_instance: BookShelf = shelf_repository.getShelfById(id)
        logger.info("Successfully fetched book ", shelf_instance)
        return response_success(shelf_instance.toJson())
