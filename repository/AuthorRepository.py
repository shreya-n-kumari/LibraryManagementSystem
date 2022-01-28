from sqlalchemy import func

from repository import Session
from model.Author import Author


class AuthorRepository:

    def getAuthorById(self, id):
        session = Session()
        return session.query(Author).filter(Author.author_id == id).first()

    def getAuthorByName(self, name):
        session = Session()
        return session.query(Author).filter(Author.author_name == name).first()

    def isAuthorExist(self, id):
        session = Session()
        return session.query(func.count(Author.author_id)).filter(Author.author_id == id).scalar() == 1

    def save(self, author_list):
        session = Session()
        session.bulk_save_objects(author_list, return_defaults=True)
        session.commit()
        session.flush()
        return author_list

    def updateAuthorById(self, id, update_request):
        session = Session()
        session.query(Author).filter(Author.author_id == id).update(update_request)
        session.commit()
        session.flush()
        return self.getAuthorById(id)

