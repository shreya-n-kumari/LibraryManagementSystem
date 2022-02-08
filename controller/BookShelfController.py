import json

from flask import Response, request
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


class ShelfSearchById(Resource):    #ERROR

    def get(self, id):
        logger.info("Fetching bookshelf with id {}".format(id))
        shelf_instance: BookShelf = shelf_repository.getShelfById(id)
        logger.info("Successfully fetched book ", shelf_instance)
        return response_success(shelf_instance.toJson())


class ShelfSearchByName(Resource):

    def get(self,name):
        logger.info("Fetching author with name {}".format(name))
        shelf_instance = shelf_repository.getShelfByName(name)
        for instance in shelf_instance:
            shelf_list = [instance.toJson()]
        logger.info("successfully Fetched Author", shelf_list)
        return response_success(shelf_list)


class ShelfInsert(Resource):

    def post(self):
        logger.info("Request to save new bookshelf")
        request_data = request.get_json()
        ShelfList = []
        for data in request_data:
            Shelf = BookShelf()
            Shelf.set_name(data["self_name"])
            Shelf.set_row(data["self_rows"])
            Shelf.set_column(data["self_columns"])
            ShelfList.append(Shelf)
        Shelf_saved: list = shelf_repository.saveShelf(ShelfList)
        Shelf_List = []
        for instance in Shelf_saved:
            Shelf_List.append([instance.toJson()])
        return response_success(Shelf_List, 200)


class ShelfUpdateById(Resource):
    def put(self, id):          #ERROR
        request_data = request.get_json()
        if shelf_repository.isShelfExist(id):
            shelf: BookShelf = shelf_repository.updateShelf(id, request_data)
        else:
            return response_failure("bookshelf id {} not found.".format(id))
        return response_success(shelf.toJson())

