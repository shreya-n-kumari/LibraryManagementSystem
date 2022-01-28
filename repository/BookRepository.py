from sqlalchemy import func

from repository import Session
from model.Book import Book


class BookRepository:

    def isBookExist(self, id):
        session = Session()
        try:
            return session.query(func.count(Book.id)).filter(Book.id == id).scalar() == 1
        finally:
            session.close()

    def getBookById(self, id):
        session = Session()
        try:
            return session.query(Book).filter(Book.id == id).first()
        finally:
            session.close()

    def getBookByName(self, name):
        session = Session()
        try:
            return session.query(Book).filter(Book.name == name).all()
        finally:
            session.close()

    def save(self, books):
        session = Session()
        try:
            session.bulk_save_objects(books, return_defaults=True)
            session.commit()
            session.flush()
            return books
        finally:
            session.close()

    def updateBookById(self, id, update_request):
        session = Session()
        try:
            session.query(Book).filter(Book.id == id).update(update_request)
            session.commit()
            session.flush()
            return self.getBookById(id)
        finally:
            session.close()

    def deleteBookById(self, id):
        pass