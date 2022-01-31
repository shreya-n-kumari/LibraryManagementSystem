import json

from flask import Response, request
from flask_restful import Resource
import logging as logger

from model.Author import Author
from repository.AuthorRepository import AuthorRepository

#Author dao global variable.

author_repository = AuthorRepository()


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

"""
    search a author by id,
    This will return only one author as author is being searched on primary key.
"""


class AuthorSearchById(Resource):

    def get(self, id):
        logger.info("Fetching author with id {}".format(id))
        author_instance: Author = author_repository.getAuthorById(id)
        logger.info("successfully Fetched Author", author_instance)
        return response_success(author_instance.toJson())


class AuthorSearchByName(Resource):

    def get(self, name):
        logger.info("Fetching author with name {}".format(name))
        author_instance = author_repository.getAuthorByName(name)
        for instance in author_instance:
            author_List = [instance.toJson()]
        logger.info("successfully Fetched Author", author_List)
        return response_success(author_List)


class AuthorInsert(Resource):

    def post(self):
        logger.info("Request to save a new author")
        request_data = request.get_json()
        authorList = []
        for data in request_data:
            author = Author()
            author.set_author_name(data["author_name"])
            authorList.append(author)
        author_saved: list = author_repository.save(authorList)
        author_list = []
        for instance in author_saved:
            author_list.append(instance.toJson())
        return response_success(author_list, 201)


class AuthorUpdateById(Resource):

    def put(self, id):
        logger.info("Request to update a Author by id: ", id)
        request_data = request.get_json()
        if author_repository.isAuthorExist(id):
            #update Author
            author: Author = author_repository.updateAuthorById(id, request_data)
        else:
           return response_failure("Author id {} not found".format(id))
        return response_success(author.toJson())






