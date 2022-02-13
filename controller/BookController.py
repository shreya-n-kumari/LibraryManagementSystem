import json

from flask import Response, request
from flask_restful import Resource
import logging as logger

from model.Author import Author
from repository.AuthorRepository import AuthorRepository
from repository.BookRepository import BookRepository
from model.Book import Book

"""
    book dao global variable
"""

book_repository = BookRepository()
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
    search a book by id,
    This will return only one book as book is being searched on primary key
"""


class BookSearchById(Resource):

    def get(self, id):
        logger.info("Fetching book with id {}".format(id))
        book_instance: Book = book_repository.getBookById(id)
        logger.info("Successfully fetched book ", book_instance)
        return response_success(book_instance.toJson())


"""
    search a book by name, 
    This may return multiple books with same name belonging to different author
"""


class BookSearchByName(Resource):

    def get(self, name: str):
        logger.info("Fetching book with name {}".format(name))
        book_instance = book_repository.getBookByName(name)
        for instance in book_instance:
            book_list = [instance.toJson()]
        logger.info("Successfully fetched book ", book_list)
        return response_success(book_list)


"""
    save multiple books as well. The post will method will pass list of book request 
    Algo:- 
    1. we must validate the book object which should at least include the author_id
    2. Query the author_id into database to check if exist, if not fail the save.
"""


class BookInsert(Resource):

    def post(self):
        logger.info("Request to save a new book")
        '''
            1. accept List of books request
            2. each book request may contains below:-
                a. only author_id in each book request in the list
                b. only new author in each book request
                c. combination of above a & b
        '''
        request_data_list = request.get_json()  # getting data from client
        isValidationFailed = False
        bookList = []
        for request_data in request_data_list:
            book = Book()
            book.set_name(request_data["name"])
            book.set_quantity(request_data["quantity"])
            book.set_description(request_data["description"])
            book.set_publication_year(request_data["publication_year"])
            book.set_publication_name(request_data["publication_name"])

            if "author_id" in request_data:
                if author_repository.isAuthorExist(request_data["author_id"]):
                    author_id = request_data["author_id"]
                else:
                    isValidationFailed = True
                    break
            else:
                author = Author()
                author.set_author_name(request_data["author"]["author_name"])
                authorDbInstance = author_repository.save([author])
                author_id = authorDbInstance[0].get_author_id()
            book.set_author_id(author_id)
            bookList.append(book)
        if isValidationFailed:
            response_failure("Invalid Input")
        # pass list of books
        book_saved: list = book_repository.save(bookList)
        for book_instance in book_saved:
            author: Author = author_repository.getAuthorById(book_instance.get_author_id())
            book_instance.set_author(Author.toModel(author))
            book_list = [book_instance.toJson()]
        return response_success(book_list, 201)


"""
    Update book by id
"""


class BookUpdateById(Resource):

    def put(self, id):
        logger.info("Request to update a book by id: ", id)
        request_data = request.get_json()
        if book_repository.isBookExist(id):
            if "author_id" in request_data:
                author_id = request_data["author_id"]
                if not author_repository.isAuthorExist(author_id):
                    return response_failure("invalid author id: {} provided".format(author_id), 500)
            # update book code
            book: Book = book_repository.updateBookById(id, request_data)
        else:
            return response_failure("book id: {} not found".format(id), 404)
        return response_success(book.toJson())


class BookDeleteById(Resource):

    def delete(self, id: int):
        logger.info("Request to delete a book by id: ", id)
        if book_repository.isBookExist(id):
            book_instance: Book = book_repository.deleteBookById(id)
        logger.info("Successfully fetched book ", book_instance)
        response_success("book id: {} deleted".format(id), 200)

