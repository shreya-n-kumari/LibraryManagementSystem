import json

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from model import Model
from model import Author


class Book(Model):
    """
        table name
    """
    __tablename__ = "books"

    """
        database columns
    """
    id = Column('id', Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=False)
    description = Column('description', String(255))
    quantity = Column('quantity', Integer, nullable=False)
    publication_year = Column('publication_year', DateTime, nullable=False)
    publication_name = Column('publication_name', String(255), nullable=False)
    author_id = Column('author_id', Integer, ForeignKey("author.author_id", onupdate='CASCADE', ondelete='SET NULL'),
                       nullable=False)
    author = relationship('Author', backref="books")

    '''
        getter-setter
    '''

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_quantity(self):
        return self.quantity

    def get_publication_year(self):
        return self.publication_year

    def get_publication_name(self):
        return self.publication_name

    def get_author_id(self):
        return self.author_id

    def get_author(self):
        return self.author

    def set_id(self, book_id):
        self.id = book_id

    def set_name(self, name):
        self.name = name

    def set_quantity(self, quantity):
        self.quantity = quantity

    def set_description(self, description):
        self.description = description

    def set_publication_year(self, publication_year):
        self.publication_year = publication_year

    def set_publication_name(self, publication_name):
        self.publication_name = publication_name

    def set_author_id(self, authorid):
        self.author_id = authorid

    def set_author(self, author: Author):
        self.author = author

    def toJson(self):
        return json.dumps({"id": self.id, "name": self.name, "description": self.description,
                           "quantity": self.quantity, "publication_year": str(self.publication_year),
                           "publication_name": self.publication_name, "author_id": self.author_id,
                           "author": self.author.toJson()}, sort_keys=True, indent=4)

    def toModel(obj):
        book = Book()
        book.id = obj.get_id()
        book.name = obj.get_name()
        book.quantity  = obj.get_quantity()
        book.description =  obj.get_description()
        book.publication_name = obj.get_publication_name()
        book.publication_year = obj.get_publication_year()
        book.author_id = obj.get_author_id()
        book.author = Author.Author.toModel(obj.get_author())
        return book