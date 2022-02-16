from sqlalchemy import func

from model.DrawerEntity import Drawer
from repository import Session


class DrawerRepository:

    def isDrawerExist(self, _id):
        session = Session()
        return session.query(func.count(Drawer.drawer_id)).filter(Drawer.drawer_id == _id).scalar() == 1

    def getDrawerById(self, _id):
        session = Session()
        return session.query(Drawer).filter(Drawer.drawer_id == _id).first()

    def save(self, drawers):
        session = Session()
        session.bulk_save_objects(drawers, return_defaults=True)
        session.commit()
        session.flush()
        return drawers

    def updateDrawerById(self, id, update_request):
        session = Session()
        session.query(Drawer).filter(Drawer.drawer_id == id).update(update_request)
        session.commit()
        session.flush()
        return self.getDrawerById(id)

    def deleteDrawerById(self, id):
        session = Session()
        x = session.query(Drawer).get(id)
        session.delete(x)
        session.commit()
        session.flush()
        return self.getDrawerById(id)

