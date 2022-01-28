from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

"""
    doa module
"""
engine = create_engine("mysql://root:password@127.0.0.1/college_library", echo=True)
Session = scoped_session(sessionmaker(autocommit=False,
                                      autoflush=False,
                                      bind=engine))
#meta = MetaData()
#meta.create_all(engine)
