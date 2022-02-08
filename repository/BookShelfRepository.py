from  sqlalchemy import func

from repository import Session
from model.BookShelf import BookShelf


class ShelfRepository:

    def isShelfExist(self, id):
        session = Session()
        return session.query(func.count(BookShelf.id)).filter(BookShelf.id == id).scalar() == 1

    def getShelfById(self, id):
        session = Session()
        return session.query(BookShelf).filter(BookShelf.id == id).first()

    def getShelfByName(self, name):
        session = Session()
        return session.query(BookShelf).filter(BookShelf.name == name).all()

    def saveShelf(self, shelf):
        session = Session()
        session.bulk_save_objects(shelf, return_defaults=True)
        session.commit()
        session.flush()
        return shelf

    def updateShelf(self, id, update_request):
        session = Session()
        session.query(BookShelf).filter(BookShelf.id == id).update(update_request)
        session.commit()
        session.flush()
        return self.getShelfById(id)

