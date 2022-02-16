import json
import logging as logger

from flask import Response, request
from flask_restful import Resource

from model.BookShelf import BookShelf
from model.DrawerEntity import Drawer
from repository.BookShelfRepository import ShelfRepository
from repository.DrawerRepository import DrawerRepository

'''
    Drawer dao global variable
'''


drawer_repository = DrawerRepository()
bookshelf_repository = ShelfRepository()


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


class DrawerSearchById(Resource):

    def get(self, id):
        logger.info("Fetching Drawer by id {}".format(id))
        drawer_instance: Drawer = drawer_repository.getDrawerById(id)
        logger.info("Successfully Fetched Drawer", drawer_instance)
        return response_success(drawer_instance.toJson())


class DrawerInsert(Resource):

    def post(self):
        logger.info("Request to save a new drawer")
        request_data_List = request.get_json()
        IsValidationFailed = False
        drawer_List = []

        for request_data in request_data_List:
            drawer = Drawer()
            drawer.set_capacity(request_data["drawer_capacity"])

            if "self_id" in request_data:
                if bookshelf_repository.isShelfExist(request_data["self_id"]):
                    shelf_id = request_data["self_id"]
                else:
                    IsValidationFailed = True
                    break
            else:
                bookshelf = BookShelf()
                bookshelf.set_name(request_data["bookshelf"]["self_name"])
                bookshelf.set_row(request_data["bookshelf"]["self_rows"])
                bookshelf.set_column(request_data["bookshelf"]["self_columns"])
                bookshelfInstance = bookshelf_repository.saveShelf([bookshelf])
                shelf_id = bookshelfInstance[0].getId()
            drawer.set_shelf_id(shelf_id)
            drawer_List.append(drawer)
        if IsValidationFailed:
            return response_failure("Invalid Input")

        # pass list of drawers
        drawer_saved: list = drawer_repository.save(drawer_List)
        for drawer_instance in drawer_saved:
            drawerList = [drawer_instance.toJson()]
        return response_success(drawerList, 201)


class DrawerUpdateById(Resource):

    def put(self, id):
        logger.info("Request to update drawer by id", id)
        request_data = request.get_json()
        if drawer_repository.isDrawerExist(id):
            drawer: Drawer = drawer_repository.updateDrawerById(id, request_data)
        else:
            response_failure("Drawer id: {} not found.".format(id), 404)
        response_success(drawer.toJson())


class DrawerDeleteById(Resource):

    def delete(self, id):       # ERROR:  does not delete 1st id.
        logger.info("Request to delete drawer by id", id)
        if drawer_repository.isDrawerExist(id):
            drawer: Drawer = drawer_repository.deleteDrawerById(id)
            logger.info("successfully deleted drawer ",drawer)
        else:
            return response_failure("drawer id {} does not exist".format(id))
        response_success("drawer id {} deleted".format(id))

