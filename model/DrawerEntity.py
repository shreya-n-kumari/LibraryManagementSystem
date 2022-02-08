import json

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

    'getter setter code'

    def get_drawer_id(self):
        return self.drawer_id

    def get_capacity(self):
        return self.capacity

    def get_shelf_id(self):
        return self.shelf_id

    def set_drawer_id(self, _id):
        self.drawer_id = _id

    def set_capacity(self, capacity):
        self.capacity = capacity

    def set_shelf_id(self, shelf_id):
        self.shelf_id = shelf_id

    def set_bookshelf(self, bookshelf: BookShelf):
        self.bookshelf = bookshelf

    def toJson(self):
        return json.dumps({"drawer_id": self.drawer_id, "drawer_capacity": self.capacity, "self_id": self.shelf_id},
                          sort_keys=True, indent=4)

    def toModel(obj):
        drawer = Drawer()
        drawer.drawer_id = obj.get_drawer_id()
        drawer.capacity = obj.get_capacity()
        drawer.shelf_id = obj.get_shelf_id()
        return drawer

