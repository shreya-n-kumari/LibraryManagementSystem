from sqlalchemy import func

from repository import Session
from model.Author import Author


class AuthorRepository:

    def getAuthorById(self, id):
        session = Session()
        try:
            return session.query(Author).filter(Author.author_id == id).first()
        finally:
            session.close()

    def getAuthorByName(self, name):
        session = Session()
        try:
            return session.query(Author).filter(Author.author_name == name).first()
        finally:
            session.close()

    def isAuthorExist(self, id):
        session = Session()
        try:
            return session.query(func.count(Author.author_id)).filter(Author.author_id == id).scalar() == 1
        finally:
            return session.close()

    def save(self, author_list):
        session = Session()
        try:
            session.bulk_save_objects(author_list, return_defaults=True)
            session.commit()
            session.flush()
            return author_list
        finally:
            session.close()

    def updateAuthorById(self, id, update_request):
        session = Session()
        try:
            session.query(Author).filter(Author.id == id).update(update_request)
            session.commit()
            session.flush()
            return self.getAuthorById(id)
        finally:
            session.close()
