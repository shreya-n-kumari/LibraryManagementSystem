import json

from sqlalchemy import Column, Integer, String

from model import Model


class BookShelf(Model):
    # Table Name
    __tablename__ = "book_self"

    # database column
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    row = Column('row', Integer, nullable=False)
    column = Column('column', Integer, nullable=False)

    def getId(self):
        return self.self_id

    def getName(self):
        return self.self_name

    def getRows(self):
        return self.self_rows

    def getColumns(self):
        return self.self_columns

    def set_id(self, _id):
        self.id = _id

    def set_name(self, name):
        self.name = name

    def set_row(self, row):
        self.rows = row

    def set_column(self, column):
        self.columns = column

    def toJson(self):
        return json.dumps({"self_id": self.id, "self_name": self.name, "self_rows": self.row, "self_columns": self.column},
                          sort_keys=True, indent=4)

    def toModel(obj):
        book = BookShelf()
        book.id = obj.id
        book.name = obj.name
        return book
