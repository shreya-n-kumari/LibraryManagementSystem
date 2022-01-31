from flask_restful import Api
from main import flaskAppInstance
from .BookController import BookSearchById, BookSearchByName, BookInsert, BookUpdateById, BookDeleteById
from .AuthorController import AuthorSearchById, AuthorSearchByName, AuthorInsert, AuthorUpdateById
from .BookShelfController import ShelfSearchById, ShelfSearchByName, ShelfInsert, ShelfUpdateById

"""
    controller module
"""
restServer = Api(flaskAppInstance)

restServer.add_resource(BookSearchById, "/api/books/<int:id>")  # get by id request
restServer.add_resource(BookSearchByName, "/api/books/<name>")  # get by name request
restServer.add_resource(BookInsert, "/api/books")  # save request
restServer.add_resource(BookUpdateById, "/api/books/<int:id>")  # update request
restServer.add_resource(BookDeleteById, "/api/books/<int:id>")  # delete request

# Authors resources
restServer.add_resource(AuthorSearchById, "/api/authors/<int:id>")  # get by id request
restServer.add_resource(AuthorSearchByName, "/api/authors/<name>")  # get by name request
restServer.add_resource(AuthorInsert, "/api/authors")  # save request
restServer.add_resource(AuthorUpdateById, "/api/authors/<int:id>")  # update request

# BookShelf resources
restServer.add_resource(ShelfSearchById, "/api/shelf/<int:id>")  # get by id request
restServer.add_resource(ShelfSearchByName, "/api/shelf/<name>")  # get by name request
restServer.add_resource(ShelfInsert, "/api/shelf")  # save request
restServer.add_resource(ShelfUpdateById, "/api/shelf/<int:id>")  # update request
