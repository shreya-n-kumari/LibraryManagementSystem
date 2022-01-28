from sqlalchemy import func

from repository import Session
from model.Book import Book


class BookRepository:

    def isBookExist(self, id):
        session = Session()
        return session.query(func.count(Book.id)).filter(Book.id == id).scalar() == 1

    def getBookById(self, id):
        session = Session()
        return session.query(Book).filter(Book.id == id).first()

    def getBookByName(self, name):
        session = Session()
        return session.query(Book).filter(Book.name == name).all()

    def save(self, books):
        session = Session()
        session.bulk_save_objects(books, return_defaults=True)
        session.commit()
        session.flush()
        return books

    def updateBookById(self, id, update_request):
        session = Session()
        session.query(Book).filter(Book.id == id).update(update_request)
        session.commit()
        session.flush()
        return self.getBookById(id)

    def deleteBookById(self, id):
        pass