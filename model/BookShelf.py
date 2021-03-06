import json

from sqlalchemy import Column, Integer, String

from model import Model


class BookShelf(Model):
    # Table Name
    __tablename__ = "book_self"

    # database column
    id = Column('self_id', Integer, primary_key=True, autoincrement=True)
    name = Column('self_name', String, nullable=False)
    row = Column('self_rows', Integer, nullable=False)
    column = Column('self_columns', Integer, nullable=False)

    def getId(self):
        return self.id

    def getName(self):
        return self.name

    def getRows(self):
        return self.row

    def getColumns(self):
        return self.column

    def set_id(self, _id):
        self.id = _id

    def set_name(self, name):
        self.name = name

    def set_row(self, row):
        self.row = row

    def set_column(self, column):
        self.column = column

    def toJson(self):
        return json.dumps({"self_id": self.id, "self_name": self.name, "self_rows": self.row,
                           "self_columns": self.column}, sort_keys=True, indent=4)

    def toModel(obj):
        book = BookShelf()
        book.id = obj.id
        book.name = obj.name
        book.row = obj.row
        book.column = obj.column
        return book
