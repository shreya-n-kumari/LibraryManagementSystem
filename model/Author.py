import json

from sqlalchemy import Column, Integer, String

from model import Model

"""
	just return the normal self model
"""


class Author(Model):
    __tablename__ = "author"

    author_id = Column('author_id', Integer, primary_key=True, autoincrement=True)
    author_name = Column('author_name', String(255), nullable=False)

    def get_author_id(self):
        return self.author_id

    def get_author_name(self):
        return self.author_name

    def set_author_id(self, id):
        self.author_id = id

    def set_author_name(self, name):
        self.author_name = name

    def toJson(self):
        return json.dumps({"author_id": self.author_id, "author_name": self.author_name},
                          sort_keys=True, indent=4)

    def toModel(obj):
        author = Author()
        author.author_id = obj.author_id
        author.author_name = obj.author_name
        return author
