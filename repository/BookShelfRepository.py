from  sqlalchemy import func

from repository import Session
from model import BookShelf

class ShelfRepository:

    def isShelfExist(self, id):
        session = Session()
        return session.query(func.count(BookShelf.id)).filter(BookShelf.id == id).scalar() == 1

    def getShelfById(self, id):
        session = Session()
        return session.query(BookShelf).filter(BookShelf.id == id).first()
