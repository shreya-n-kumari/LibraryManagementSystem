from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from model import Model
from model import BookShelf


class Drawer(Model):

    __tablename__ = "drawers"

    drawer_id = Column('drawer_id', Integer, primary_key=True, autoincrement=True)
    capacity = Column('drawer_capacity', Integer, nullable=False)
    shelf_id = Column('self_id', Integer, ForeignKey("book_self.self_id", onupdate='CASCADE', ondelete='SET NULL'),
                      nullable=False)
    bookshelf = relationship('BookShelf', backref = "book_self")

    #getter setter code

    def get_drawer_id(self):
        return self.drawer_id
    